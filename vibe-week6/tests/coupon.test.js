const test = require('node:test');
const assert = require('node:assert/strict');

const { applyCoupon } = require('../src/payments/coupon');

test('applies a percentage coupon discount to a price', () => {
  assert.equal(applyCoupon(10000, 20), 8000);
});

test('throws when the coupon rate is zero or less', () => {
  assert.throws(() => applyCoupon(10000, 0));
  assert.throws(() => applyCoupon(10000, -1));
});

test('throws when the coupon rate is greater than 100', () => {
  assert.throws(() => applyCoupon(10000, 101));
});
