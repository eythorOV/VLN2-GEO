// Get all filter buttons
const filterButtons = document.querySelectorAll('.filter_button');
      
// Add event listener to each filter button
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        const filterType = button.classList[1]; // Get the class name of the filter button

        // Show or hide pizzas based on the selected filter
        const pizzas = document.querySelectorAll('.block');
        pizzas.forEach(pizza => {
            const isSpicy = pizza.dataset.spicy === 'true';
            const isVegan = pizza.dataset.vegan === 'true';
            const isDesert = pizza.dataset.desert === 'true';
            const isPopular = pizza.dataset.popular === 'true';

            if (
                filterType === 'all' ||
                (filterType === 'spicy' && isSpicy) ||
                (filterType === 'vegan' && isVegan) ||
                (filterType === 'desert' && isDesert) ||
                (filterType === 'popular' && isPopular)
            ) {
                pizza.style.display = 'block';
            } else {
                pizza.style.display = 'none';
            }
        });
    });
});

// Get the name and price buttons
const nameButton = document.getElementById('name');
const priceButton = document.getElementById('price');

// Add event listener to the name button
nameButton.addEventListener('click', () => {
    const pizzas = document.querySelectorAll('.block');
    const sortedPizzas = Array.from(pizzas).sort((a, b) => {
        const nameA = a.querySelector('#pizza_name').textContent.toLowerCase();
        const nameB = b.querySelector('#pizza_name').textContent.toLowerCase();
        return nameA.localeCompare(nameB);
    });
    displaySortedPizzas(sortedPizzas);
});

// Add event listener to the price button
priceButton.addEventListener('click', () => {
    const pizzas = document.querySelectorAll('.block');
    const sortedPizzas = Array.from(pizzas).sort((a, b) => {
        const priceA = parseFloat(a.querySelector('#pizza_price').textContent.replace(/[^0-9.-]+/g, ''));
        const priceB = parseFloat(b.querySelector('#pizza_price').textContent.replace(/[^0-9.-]+/g, ''));
        return priceA - priceB;
    });
    displaySortedPizzas(sortedPizzas);
});

// Helper function to display sorted pizzas
function displaySortedPizzas(pizzas) {
    const menuContainer = document.querySelector('.menu_container');
    menuContainer.innerHTML = ''; // Clear the current menu container

    pizzas.forEach(pizza => {
        menuContainer.appendChild(pizza);
    });
}

// Get the search input and search button
const searchInput = document.getElementById('text_field');
const searchButton = document.querySelector('.search_button');

// Add event listener to the search button
searchButton.addEventListener('click', () => {
const searchTerm = searchInput.value.toLowerCase().trim();
searchPizzas(searchTerm);
});

// Function to search and display pizzas based on the search term
function searchPizzas(searchTerm) {
const pizzas = document.querySelectorAll('.block');
pizzas.forEach(pizza => {
  const pizzaName = pizza.querySelector('#pizza_name').textContent.toLowerCase();
  if (pizzaName.includes(searchTerm)) {
      pizza.style.display = 'block';
  } else {
      pizza.style.display = 'none';
  }
});
}