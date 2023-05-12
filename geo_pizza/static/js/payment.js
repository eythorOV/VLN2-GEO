// Validate credit card information
const cardHolderNameInput = document.getElementById('cardHolderName');
const cardNumberInput = document.getElementById('cardNumber');
const expirationDateInput = document.getElementById('expirationDate');
const cvcNumberInput = document.getElementById('cvcNumber');

function validateCreditCard() {
  // Remove any previous error messages
  cardHolderNameInput.nextElementSibling.textContent = '';
  cardNumberInput.nextElementSibling.textContent = '';
  expirationDateInput.nextElementSibling.textContent = '';
  cvcNumberInput.nextElementSibling.textContent = '';

  // Validate card holder name (not empty)
  if (cardHolderNameInput.value.trim() === '') {
    cardHolderNameInput.nextElementSibling.textContent = 'Please enter the card holder name.';
    return false;
  }

  // Validate credit card number (16 digits)
  const cardNumber = cardNumberInput.value.replace(/\s/g, '');
  if (!/^\d{16}$/.test(cardNumber)) {
    cardNumberInput.nextElementSibling.textContent = 'Please enter a valid 16-digit credit card number.';
    return false;
  }

  // Validate expiration date (format: MM/YY)
  const expirationDate = expirationDateInput.value.trim();
  if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(expirationDate)) {
    expirationDateInput.nextElementSibling.textContent = 'Please enter a valid expiration date in the format MM/YY.';
    return false;
  }

  // Validate CVC number (3 digits)
  const cvcNumber = cvcNumberInput.value.trim();
  if (!/^\d{3}$/.test(cvcNumber)) {
    cvcNumberInput.nextElementSibling.textContent = 'Please enter a valid 3-digit CVC number.';
    return false;
  }

  return true;
}

// Attach the validation function to the form's submit event
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
  if (!validateCreditCard()) {
    event.preventDefault(); // Prevent form submission if validation fails
  }
});
