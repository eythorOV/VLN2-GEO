const addToCartButtons = document.querySelectorAll('.add_to_cart');
addToCartButtons.forEach(button => {
    button.addEventListener('click', event => {
        console.log('clicked');
        event.preventDefault(); // prevent form submission
        const form = event.target.closest('form');
        const productType = 'Pizza';
        console.log(productType);
        getAttributebyName
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
    });
});


function add_to_cart(button) {
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