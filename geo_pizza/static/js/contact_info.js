const form = document.getElementById('contactForm');
  const firstNameError = document.getElementById('firstnameError');
  const lastNameError = document.getElementById('lastnameError');
  const streetError = document.getElementById('streetError');
  const houseNumberError = document.getElementById('housenumberError');
  const cityError = document.getElementById('cityError');
  const postalcodeError = document.getElementById('postalcodeError');

  form.addEventListener('submit', (event) => {
    // Clear previous error messages
    firstNameError.textContent = '';
    lastNameError.textContent = '';
    streetError.textContent = '';
    houseNumberError.textContent = '';
    cityError.textContent = '';
    postalcodeError.textContent = '';

    const firstName = form.firstname.value;
    const lastName = form.lastname.value;
    const street = form.street.value;
    const houseNumber = form.housenumber.value;
    const city = form.city.value;
    const postalcode = form.postalcode.value;

    if (!firstName) {
      event.preventDefault();
      firstNameError.textContent = 'Please enter your first name.';
    }

    if (!lastName) {
      event.preventDefault();
      lastNameError.textContent = 'Please enter your last name.';
    }

    if (!street) {
      event.preventDefault();
      streetError.textContent = 'Please enter the street name.';
    }

    if (!city) {
      event.preventDefault();
      cityError.textContent = 'Please enter the city name.';
    }

    if (!houseNumber) {
      event.preventDefault();
      houseNumberError.textContent = 'Please enter the house number.';
    } else if (!Number.isInteger(Number(houseNumber))) {
      event.preventDefault();
      houseNumberError.textContent = 'House number must be an integer.';
    }

    if (!postalcode) {
      event.preventDefault();
      postalcodeError.textContent = 'Please enter the postal code.';
    } else if (!Number.isInteger(Number(postalcode))) {
      event.preventDefault();
      postalcodeError.textContent = 'Postal code must be an integer.';
    }

  });