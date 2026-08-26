function applyCoupon(price, rate) {
  if (rate <= 0 || rate > 100) {
    throw new Error('rate must be greater than 0 and at most 100');
  }

  return price * (1 - rate / 100);
}

module.exports = { applyCoupon };
