# Codex Project Guidelines

- 절대 위반 금지 규칙은 @GOLDEN_RULES.md를 따른다.
- 활성 결제 코드는 `src/payments/`에만 있다.
- `src/billing/`과 `src/old/`는 폐기 예정(DEPRECATED)이므로 절대 수정하거나 참조하지 않는다.
- 모든 금액은 최소 화폐 단위(minor unit)의 정수로 다룬다.
- 모든 결제 관련 로그는 `lib/logger.js`의 `logPayment()`만 사용한다.
- 코드 변경 후 반드시 `npm test`를 실행하고 통과를 확인한다.
- 자세한 결제 규칙은 @docs/payment-rules.md를 따른다.
