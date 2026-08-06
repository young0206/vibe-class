# Golden Rules

1. 활성 결제 코드는 `src/payments/`에만 둔다.
2. `src/billing/`과 `src/old/`의 코드를 수정하거나 참조하지 않는다.
3. 모든 금액은 최소 화폐 단위(minor unit)의 정수로 다룬다.
4. 모든 결제 로그는 `lib/logger.js`의 `logPayment()`만 사용한다.
5. 코드 변경 후 반드시 `npm test`를 실행하고 통과를 확인한다.
