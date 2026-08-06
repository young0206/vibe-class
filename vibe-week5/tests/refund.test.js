const test = require('node:test');
const assert = require('node:assert/strict');
const { refund } = require('../src/payments/refund');

test('refunds a normal payment in minor units', () => {
  const result = refund({ id: 'order-100', amountMinor: 12500, currency: 'KRW' });

  assert.deepEqual(result, {
    orderId: 'order-100',
    originalAmountMinor: 12500,
    feeMinor: 625,
    refundAmountMinor: 11875,
    currency: 'KRW',
    status: 'refunded'
  });
});

test('floors a fractional five-percent fee and defaults currency to KRW', () => {
  const result = refund({ id: 'order-103', amountMinor: 101 });

  assert.deepEqual(result, {
    orderId: 'order-103',
    originalAmountMinor: 101,
    feeMinor: 5,
    refundAmountMinor: 96,
    currency: 'KRW',
    status: 'refunded'
  });
});

test('logs the original amount, fee, and actual refund amount', () => {
  const originalConsoleLog = console.log;
  const messages = [];
  console.log = (message) => messages.push(message);

  try {
    refund({ id: 'order-104', amountMinor: 199, currency: 'USD' });
  } finally {
    console.log = originalConsoleLog;
  }

  assert.equal(messages.length, 1);
  const logEntry = JSON.parse(messages[0]);
  assert.deepEqual(
    {
      event: logEntry.event,
      order_id: logEntry.order_id,
      original_amount_minor: logEntry.original_amount_minor,
      fee_minor: logEntry.fee_minor,
      refund_amount_minor: logEntry.refund_amount_minor,
      currency: logEntry.currency,
      status: logEntry.status
    },
    {
      event: 'payment.refunded',
      order_id: 'order-104',
      original_amount_minor: 199,
      fee_minor: 9,
      refund_amount_minor: 190,
      currency: 'USD',
      status: 'refunded'
    }
  );
});

test('rejects a zero amount', () => {
  assert.throws(
    () => refund({ id: 'order-101', amountMinor: 0, currency: 'KRW' }),
    /greater than zero/
  );
});

test('rejects a negative amount', () => {
  assert.throws(
    () => refund({ id: 'order-102', amountMinor: -100, currency: 'KRW' }),
    /greater than zero/
  );
});

test('rejects a non-integer amount', () => {
  assert.throws(
    () => refund({ id: 'order-105', amountMinor: 100.5, currency: 'KRW' }),
    TypeError
  );
});

test('rejects an unsafe integer amount without logging success', () => {
  const originalConsoleLog = console.log;
  let logCount = 0;
  console.log = () => { logCount += 1; };

  try {
    assert.throws(
      () => refund({ id: 'order-106', amountMinor: Number.MAX_SAFE_INTEGER + 1 }),
      TypeError
    );
  } finally {
    console.log = originalConsoleLog;
  }

  assert.equal(logCount, 0);
});
