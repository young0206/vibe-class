const logger = require('../../lib/logger');

// New payments code stores every amount as an integer minor-unit value.
const refund = (order) => {
  if (order == null) {
    throw new TypeError('An order is required');
  }

  const amount = order.amountMinor;
  if (!Number.isSafeInteger(amount)) {
    throw new TypeError('Refund amount must be a safe integer in minor units');
  }
  if (amount <= 0) {
    throw new RangeError('Refund amount must be greater than zero');
  }

  const feeMinor = Math.floor(amount / 20);
  const refundAmountMinor = amount - feeMinor;
  if (!Number.isSafeInteger(feeMinor) || !Number.isSafeInteger(refundAmountMinor)) {
    throw new RangeError('Calculated refund amounts are outside the safe integer range');
  }

  const refundRecord = {
    orderId: order.id,
    originalAmountMinor: amount,
    feeMinor,
    refundAmountMinor,
    currency: order.currency || 'KRW',
    status: 'refunded'
  };

  logger.logPayment('payment.refunded', refundRecord);
  return refundRecord;
};

module.exports = { refund };
