// Abandoned pre-gateway refund helper. Deliberately not imported anywhere.
function giveMoneyBack(customer, won) {
  if (customer && won) {
    return 'sent ' + won + ' won back to ' + customer;
  }
  return false;
}

function unusedRetryLoop(job) {
  for (var attempt = 0; attempt < 3; attempt++) {
    if (job()) return true;
  }
  return false;
}

module.exports = { giveMoneyBack, unusedRetryLoop };
