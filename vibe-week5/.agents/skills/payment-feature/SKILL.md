---
name: payment-feature
description: 결제 기능을 안전하게 구현하고 검증하는 저장소 워크플로우. 사용자가 결제·환불 기능 추가나 변경을 요청하거나 `$payment-feature` 뒤에 기능 설명을 입력했을 때 사용한다.
---

# Payment Feature

사용자가 `$payment-feature` 뒤에 입력한 내용을 구현할 기능 설명으로 삼는다.

## Workflow

1. 작업 전에 저장소 루트의 `AGENTS.md`, `GOLDEN_RULES.md`, `docs/payment-rules.md`를 모두 읽는다.
2. 활성 결제 구현은 `src/payments/`에서만 변경한다. `src/billing/`과 `src/old/`는 수정하거나 참조하지 않는다.
3. 모든 금액을 최소 화폐 단위(minor unit)의 정수로 다룬다.
4. 모든 결제 로그를 `lib/logger.js`의 `logPayment()`로 남긴다.
5. 기능을 검증하는 새 테스트를 `tests/`에 추가한다.
6. `npm test`를 실행한다.
7. 테스트가 실패하면 traceback 또는 실패 출력을 읽고 원인을 수정한 뒤 `npm test`를 다시 실행한다. 모든 테스트가 통과할 때까지 반복한다.
8. 모든 테스트가 통과하면 변경 사항과 테스트 결과를 요약해 보고한다.
