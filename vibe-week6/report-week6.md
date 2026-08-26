# 6주차 실습 일지 — 자산 공장

## 완료한 LAB 체크리스트

- [x] LAB 01
- [x] LAB 02
- [ ] LAB 03
- [ ] LAB 04
- [x] LAB 05
- [x] LAB 06
- [ ] LAB 07
- [ ] LAB 08
- [ ] LAB 09
- [x] LAB 10
- [ ] LAB 11

## LAB별 기록

### LAB 01
- 산출물 경로: `CLAUDE.md`
- 핵심 증거: CLAUDE.md 행동 원칙 4개 및 재구술 결과 확인
- 관찰 한 줄: Claude가 CLAUDE.md의 행동 원칙과 금지사항을 의도한 대로 이해하고 있음을 재구술을 통해 확인했다.

### LAB 02
- 산출물 경로: `.claude/skills/repo-grade/SKILL.md`
- 핵심 증거: 첫 채점 50/100 (`image/lab02-before.png`), ROI 1위 개선 후 재채점 70/100 (`image/lab02-after.png`)
- 관찰 한 줄: repo-grade로 부족한 부분을 수치로 확인하고 ROI가 가장 높은 항목을 개선한 뒤 점수가 실제로 상승하는 것을 확인했다.

### LAB 03
- [산출물 경로]
- [전/후 · 차단 등 핵심 증거(캡처 파일명)]
- [관찰 한 줄]

### LAB 04
- [산출물 경로]
- [전/후 · 차단 등 핵심 증거(캡처 파일명)]
- [관찰 한 줄]

### LAB 05
- 산출물 경로: `../luna-plugin/`
- 핵심 증거: `repo-grade`, `tdd-guard`, `bash-guard`를 별도 디렉터리로 패키징하고, 다른 테스트 저장소에서 repo-grade 실행 확인 (`image/lab05-plugin-test.png`)
- 관찰 한 줄: 한 프로젝트에서 만든 Codex용 규칙과 도구를 별도 자산으로 분리해 다른 저장소에서도 재사용할 수 있음을 확인했다.

### LAB 06
- 산출물 경로: `scripts/hooks/tdd-guard.sh`, `AGENTS.md`, `tests/coupon.test.js`, `src/payments/coupon.js`
- 핵심 증거: 테스트 없는 coupon 구현 요청 시 TDD GUARD deny 확인, RED(`MODULE_NOT_FOUND`) 후 구현, 최종 `npm test` 4개 통과
- 관찰 한 줄: Codex에서도 guard 규칙을 먼저 적용하게 하니 테스트가 없는 상태에서는 구현을 멈추고, 테스트 작성 → RED → 구현 → GREEN 순서로 진행되는 것을 확인했다.

### LAB 07
- [산출물 경로]
- [전/후 · 차단 등 핵심 증거(캡처 파일명)]
- [관찰 한 줄]

### LAB 08
- [산출물 경로]
- [전/후 · 차단 등 핵심 증거(캡처 파일명)]
- [관찰 한 줄]

### LAB 09
- [산출물 경로]
- [전/후 · 차단 등 핵심 증거(캡처 파일명)]
- [관찰 한 줄]

### LAB 10
- 산출물 경로: `scripts/hooks/bash-guard.sh`, `AGENTS.md`
- 핵심 증거: `rm -rf`, `git push --force`, `git reset --hard`, `DROP TABLE` 명령 차단 및 `ls`, `mkdir` 정상 통과 확인
- 관찰 한 줄: 위험한 Bash 명령을 실행 전에 검사하도록 하여 Codex가 실수로 파괴적인 명령을 실행하는 것을 방지할 수 있음을 확인했다.

### LAB 11
- [산출물 경로]
- [전/후 · 차단 등 핵심 증거(캡처 파일명)]
- [관찰 한 줄]

## 종합 관찰 3줄

1. 규칙을 문서로만 작성하는 것보다 guard와 테스트처럼 실제 작업 흐름에서 강제할 수 있는 장치를 함께 두는 것이 더 효과적이었다.
2. repo-grade를 이용하면 저장소가 AI 에이전트가 작업하기 좋은 상태인지 수치로 확인하고, 개선 우선순위도 정할 수 있었다.
3. 프로젝트별로 만든 규칙과 도구를 재사용 가능한 자산으로 분리하면 다른 저장소에서도 동일한 Codex 작업 방식을 적용할 수 있었다.