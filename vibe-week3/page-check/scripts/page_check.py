#!/usr/bin/env python3
"""Check one HTML file for five basic page-quality concerns."""

from __future__ import annotations

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.titles: list[tuple[int, list[str]]] = []
        self._title: tuple[int, list[str]] | None = None
        self.images: list[tuple[int, dict[str, str | None]]] = []
        self.links: list[tuple[int, str]] = []
        self.metas: list[tuple[int, dict[str, str | None]]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        line = self.getpos()[0]
        if tag == "title":
            self._title = (line, [])
            self.titles.append(self._title)
        elif tag == "img":
            self.images.append((line, values))
        elif tag == "a" and values.get("href") is not None:
            self.links.append((line, values["href"] or ""))
        elif tag == "meta":
            self.metas.append((line, values))
        if values.get("id"):
            self.ids.add(values["id"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._title = None

    def handle_data(self, data: str) -> None:
        if self._title is not None:
            self._title[1].append(data)


def add(results: list[dict[str, object]], level: str, check: str, line: int | None, message: str, action: str) -> None:
    results.append({"level": level, "check": check, "line": line, "message": message, "action": action})


def check_page(html_path: Path) -> dict[str, object]:
    raw = html_path.read_bytes()
    results: list[dict[str, object]] = []
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return {"file": str(html_path), "results": [{"level": "🔴심각", "check": "한글 인코딩(UTF-8)", "line": None, "message": f"UTF-8 디코딩 실패: {exc}", "action": "파일을 UTF-8로 다시 저장하세요."}]}

    parser = PageParser()
    parser.feed(text)

    title_ok = any("".join(parts).strip() for _, parts in parser.titles)
    if not title_ok:
        add(results, "🔴심각", "title 유무", parser.titles[0][0] if parser.titles else None, "유효한 <title>이 없습니다.", "<head>에 내용을 가진 <title>을 추가하세요.")

    for line, attrs in parser.images:
        if "alt" not in attrs:
            add(results, "🟡주의", "이미지 alt", line, "이미지에 alt 속성이 없습니다.", "의미 있는 대체 텍스트를 쓰고 장식 이미지는 alt=\"\"로 표시하세요.")

    viewport_ok = any((meta.get("name") or "").lower() == "viewport" and "width=device-width" in (meta.get("content") or "").replace(" ", "").lower() for _, meta in parser.metas)
    if not viewport_ok:
        add(results, "🟡주의", "모바일 viewport", None, "width=device-width를 포함한 viewport 메타가 없습니다.", "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">를 추가하세요.")

    charset_meta = next(((line, meta) for line, meta in parser.metas if meta.get("charset") is not None), None)
    http_equiv_utf8 = any((meta.get("http-equiv") or "").lower() == "content-type" and "charset=utf-8" in (meta.get("content") or "").replace(" ", "").lower() for _, meta in parser.metas)
    charset_ok = bool(charset_meta and (charset_meta[1].get("charset") or "").lower().replace("_", "-") == "utf-8") or http_equiv_utf8
    if not charset_ok:
        add(results, "🔴심각", "한글 인코딩(UTF-8)", charset_meta[0] if charset_meta else None, "UTF-8 인코딩 선언이 없습니다.", "<head> 앞부분에 <meta charset=\"UTF-8\">를 추가하세요.")

    external_schemes = {"http", "https", "mailto", "tel", "data", "javascript"}
    checked_targets: dict[Path, PageParser] = {html_path.resolve(): parser}
    for line, href in parser.links:
        if not href or href.startswith("//"):
            continue
        parsed = urlsplit(href)
        if parsed.scheme.lower() in external_schemes:
            continue
        target = html_path if not parsed.path else html_path.parent / unquote(parsed.path)
        if not target.exists():
            add(results, "🔴심각", "깨진 내부 링크", line, f"내부 링크 대상이 없습니다: {href}", "href 경로나 대상 파일을 바로잡으세요.")
            continue
        if parsed.fragment and target.is_file() and target.suffix.lower() in {".html", ".htm"}:
            resolved = target.resolve()
            if resolved not in checked_targets:
                linked_parser = PageParser()
                linked_parser.feed(target.read_text(encoding="utf-8"))
                checked_targets[resolved] = linked_parser
            if unquote(parsed.fragment) not in checked_targets[resolved].ids:
                add(results, "🔴심각", "깨진 내부 링크", line, f"링크 대상 fragment가 없습니다: {href}", "href의 #fragment 또는 대상 요소 id를 바로잡으세요.")

    checks_with_issues = {item["check"] for item in results}
    all_checks = {"title 유무", "깨진 내부 링크", "이미지 alt", "모바일 viewport", "한글 인코딩(UTF-8)"}
    if not results:
        add(results, "🟢제안", "전체", None, "5가지 점검 항목을 모두 통과했습니다.", "현재 상태를 유지하세요.")
    else:
        passed = sorted(all_checks - checks_with_issues)
        if passed:
            add(results, "🟢제안", "통과 항목", None, ", ".join(passed), "통과한 항목은 현재 상태를 유지하세요.")

    counts = {level: sum(item["level"] == level for item in results) for level in ("🔴심각", "🟡주의", "🟢제안")}
    return {"file": str(html_path), "counts": counts, "results": results}


def main() -> int:
    arg_parser = argparse.ArgumentParser(description="HTML 페이지의 기본 품질 5가지를 점검합니다.")
    arg_parser.add_argument("html_file", type=Path)
    args = arg_parser.parse_args()
    if not args.html_file.is_file():
        print(json.dumps({"error": f"HTML 파일을 찾을 수 없습니다: {args.html_file}"}, ensure_ascii=False, indent=2))
        return 2
    try:
        report = check_page(args.html_file.resolve())
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if any(item["level"] == "🔴심각" for item in report["results"]) else 0


if __name__ == "__main__":
    sys.exit(main())
