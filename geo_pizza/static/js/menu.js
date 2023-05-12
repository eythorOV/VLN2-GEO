document.addEventListener("DOMContentLoaded", function() {
    var filterButtons = document.querySelectorAll(".filter_button");
    var pizzaItems = document.querySelectorAll(".block");
  
    filterButtons.forEach(function(button) {
      button.addEventListener("click", function() {
        var filter = this.getAttribute("data-filter");
  
        filterButtons.forEach(function(btn) {
          btn.classList.remove("active");
        });
  
        this.classList.add("active");
  
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
  
    filterButtons[0].addEventListener("click", function() {
      pizzaItems.forEach(function(item) {
        item.classList.remove("hide");
      });
    });
  });
  

// Displays the name or price when either of the buttons are clicked
const nameButton = document.getElementById('name');
const priceButton = document.getElementById('price');

nameButton.addEventListener('click', () => {
    const pizzas = document.querySelectorAll('.block');
    const sortedPizzas = Array.from(pizzas).sort((a, b) => {
        const nameA = a.querySelector('#pizza_name').textContent.toLowerCase();
        const nameB = b.querySelector('#pizza_name').textContent.toLowerCase();
        return nameA.localeCompare(nameB);
    });
    displaySortedPizzas(sortedPizzas);
});

priceButton.addEventListener('click', () => {
    const pizzas = document.querySelectorAll('.block');
    const sortedPizzas = Array.from(pizzas).sort((a, b) => {
        const priceA = parseFloat(a.querySelector('#pizza_price').textContent.replace(/[^0-9.-]+/g, ''));
        const priceB = parseFloat(b.querySelector('#pizza_price').textContent.replace(/[^0-9.-]+/g, ''));
        return priceA - priceB;
    });
    displaySortedPizzas(sortedPizzas);
});

function displaySortedPizzas(pizzas) {
    const menuContainer = document.querySelector('.menu_container');
    menuContainer.innerHTML = '';

    pizzas.forEach(pizza => {
        menuContainer.appendChild(pizza);
    });
}

// Search bar on the menu page, listening for input
const searchInput = document.getElementById('text_field');

searchInput.addEventListener('input', () => {
    const searchTerm = searchInput.value.toLowerCase().trim();
    searchPizzas(searchTerm);
});

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
