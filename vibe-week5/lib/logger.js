function logPayment(event, data) {
  console.log(JSON.stringify({
    ts: new Date().toISOString(),
    event,
    order_id: data.orderId,
    original_amount_minor: data.originalAmountMinor,
    fee_minor: data.feeMinor,
    refund_amount_minor: data.refundAmountMinor,
    currency: data.currency,
    status: data.status
  }));
}

module.exports = { logPayment };
