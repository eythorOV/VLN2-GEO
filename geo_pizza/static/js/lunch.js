function add_to_cart(event) {
    event.preventDefault();
    console.log('clicked');
    const pizzaSelect = document.getElementById('pizza-select');
    const sodaSelect = document.getElementById('soda-select');
    const pizzaIdInput = document.getElementById('pizza-id-input');
    const sodaIdInput = document.getElementById('soda-id-input');
    const form = document.getElementById('add-to-cart-form');
    console.log(form, pizzaSelect, sodaSelect, pizzaIdInput, sodaIdInput)
    if (!form || !pizzaSelect || !sodaSelect || !pizzaIdInput || !sodaIdInput ) {
        console.error('Form or input elements not found');
        return;
    }
    const productType = form.dataset.productType;
    console.log(productType);
    const pizzaId = pizzaSelect.value;
    console.log(pizzaId);
    const sodaId = sodaSelect.value;
    console.log(sodaId);
    const url = `/offers/add_to_cart`;
    const formData = new FormData();
    formData.append('pizza_id', pizzaId);
    formData.append('soda_id', sodaId);
    formData.append('product_type', productType);

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));}