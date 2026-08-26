# Codex 작업 규칙

- Bash 명령 실행 전 위험 가능성이 있으면 `scripts/hooks/bash-guard.sh`로 검사한다.
- 검사 결과가 `BLOCKED`이면 실제 명령을 실행하지 않는다.
- 가능한 경우 차단된 명령 대신 안전한 대안을 제안한다.
- 아래의 기존 TDD 규칙을 계속 유지한다.
- `src/` 아래의 `.js` 파일을 새로 만들거나 수정하기 전에, 반드시 대상 파일 경로를 `file_path`로 전달해 `scripts/hooks/tdd-guard.sh`를 먼저 실행한다.
- guard 결과가 `deny`이면 소스 파일을 수정하지 않는다.
- `deny` 이유에 맞는 테스트를 먼저 작성하고 테스트 실패(RED)를 확인한다.
- 대응하는 테스트가 존재한 뒤에만 구현 파일을 작성한다.
- 구현 후 `npm test`를 실행해 전체 테스트 통과를 확인한다.
- 기존 `CLAUDE.md`와 `GOLDEN_RULES.md`의 원칙도 계속 따른다.
