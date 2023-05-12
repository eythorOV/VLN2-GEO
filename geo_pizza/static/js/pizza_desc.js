function add_to_cart(button, event) {
    event.preventDefault();
    console.log('clicked');
    const form = button.closest('form');
    const productType = form.dataset.productType;
    console.log(productType);
    const productId = button.value;
    console.log(productId);
    const quantity = form.elements.quantity.value;
    console.log(productType, productId, quantity);
    const url = `/menu/add_to_cart/${productType}/${productId}/${quantity}`;
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}