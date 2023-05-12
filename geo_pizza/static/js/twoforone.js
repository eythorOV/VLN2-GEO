function add_to_cart(event) {
    event.preventDefault();
    console.log('clicked');

    const pizza1Select = document.getElementById('pizza1-select');
    const pizza2Select = document.getElementById('pizza2-select');
    const sodaSelect = document.getElementById('soda-select');
    const pizzaIdInput1 = document.getElementById('pizza-id-input1');
    const pizzaIdInput2 = document.getElementById('pizza-id-input2');
    const sodaIdInput = document.getElementById('soda-id-input');
    const form = document.getElementById('add-to-cart-form');
    console.log(pizza1Select, pizza2Select, sodaSelect, pizzaIdInput1, pizzaIdInput2, sodaIdInput, form);
    if (!form || !pizza1Select || !sodaSelect || !pizza2Select || !pizzaIdInput1 || !sodaIdInput || !pizzaIdInput2) {
        console.error('Form or input elements not found');
        return;
    }
    const productType = form.dataset.productType;
    console.log(productType);
    const pizzaId1 = pizza1Select.value;
    console.log(pizzaId1);
    const pizzaId2 = pizza2Select.value;
    const sodaId = sodaSelect.value;
    console.log(sodaId);
    const url = `/offers/add_to_cart`;
    const formData = new FormData();
    formData.append('pizza1_id', pizzaId1);
    formData.append('pizza2_id', pizzaId2);
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