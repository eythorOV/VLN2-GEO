document.addEventListener("DOMContentLoaded", function() {
    var filterButtons = document.querySelectorAll(".filter_button");
    var pizzaItems = document.querySelectorAll(".block");
  
    // Add click event listener to each filter button
    filterButtons.forEach(function(button) {
      button.addEventListener("click", function() {
        var filter = this.getAttribute("data-filter");
  
        // Remove the active class from all filter buttons
        filterButtons.forEach(function(btn) {
          btn.classList.remove("active");
        });
  
        // Add the active class to the clicked filter button
        this.classList.add("active");
  
        // Show/hide pizza items based on the filter value
        pizzaItems.forEach(function(item) {
          var isSpicy = item.getAttribute("data-spicy") === "True";
          var isVegan = item.getAttribute("data-vegan") === "True";
          var isDesert = item.getAttribute("data-desert") === "True";
          var isPopular = item.getAttribute("data-popular") === "True";
  
          if (
            filter === "all" ||
            (filter === "spicy" && isSpicy) ||
            (filter === "vegan" && isVegan) ||
            (filter === "desert" && isDesert) ||
            (filter === "popular" && isPopular)
          ) {
            item.classList.remove("hide");
          } else {
            item.classList.add("hide");
          }
        });
      });
    });
  
    // Show all pizzas when the page loads
    filterButtons[0].addEventListener("click", function() {
      pizzaItems.forEach(function(item) {
        item.classList.remove("hide");
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

// Get the search input
const searchInput = document.getElementById('text_field');

// Add event listener to the search input
searchInput.addEventListener('input', () => {
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
