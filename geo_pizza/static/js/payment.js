
    function validateCreditCardNumber() {
        var ccNumber = document.getElementById('card_number').value;
        if (!/^\d{16}$/.test(ccNumber)) {
            alert("Please enter a valid 16-digit credit card number.");
            return false;
        }
        return true;
    }

    function validateExpiryDate() {
        var expDate = document.getElementById('exp_date').value;
        if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(expDate)) {
            alert("Please enter a valid expiry date in the format MM/YY.");
            return false;
        }
        return true;
    }

    function validateCVC() {
        var cvc = document.getElementById('cvc').value;
        if (!/^\d{3}$/.test(cvc)) {
            alert("Please enter a valid 3-digit CVC number.");
            return false;
        }
        return true;
    }

    function validateForm() {
        if (!validateCreditCardNumber() || !validateExpiryDate() || !validateCVC()) {
            return false;
        }
        return true;
    }