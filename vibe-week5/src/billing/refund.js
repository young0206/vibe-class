// Old billing code. Amounts in this module are whole won.
function refund(order) {
  if (!order) throw new Error('order required');
  if (order.amountWon === 0) throw new Error('cannot refund zero won');
  if (order.amountWon < 0) throw new Error('cannot refund a negative amount');

  var result = {
    orderId: order.id,
    amountWon: order.amountWon,
    status: 'refunded'
  };

  console.log('REFUND OK order=' + order.id + ' amount=' + order.amountWon + 'KRW');
  return result;
}

module.exports = { refund: refund };
