-- DELETE FROM django_migrations WHERE app='menu' AND name='0001_initial';
-- Drop table if exists menu_PizzaToppings;
-- Drop table if exists menu_Pizza;
-- Drop table if exists menu_Toppings;
-- Drop table if exists menu_Category;

INSERT INTO menu_Toppings (name, price)
VALUES ('Tomato sauce', 0), ('Cheese',0), ('Vegan cheese', 0), ('Pineapple', 345), ('Ham', 495), ('Pepperoni', 2), ('Mushrooms', 345), ('Olives', 345), ('Spinach', 345);

-- Insert pizzas
INSERT INTO menu_Pizza (name, priceSmall, priceMedium, priceLarge, spicy, vegan, desert, popular, image, description)
VALUES ('Margarita', 1000, 1200, 1500, false, false, false, true, 'margarita.jpg', 'Classic pizza with tomato sauce, mozzarella, and basil.'),
       ('Hawaiian', 1200, 1400, 1700, false, false, false, true, 'hawaiian.jpg', 'Pizza with tomato sauce, mozzarella, ham, and pineapple.'),
       ('Pepperoni and Mushrooms', 11, 13, 16, true, false, false, true, 'pepperoni-mushrooms.jpg', 'Pizza with tomato sauce, mozzarella, pepperoni, and mushrooms.'),
       ('Vegan', 13, 15, 18, false, true, false, false, 'vegan.jpg', 'Pizza with tomato sauce, vegan cheese, and a variety of vegetables.');

-- Insert pizza toppings
INSERT INTO menu_PizzaToppings (pizza_id, topping_id)
VALUES (1, 1), (1, 2), (2, 1), (2, 2), (2, 5), (2, 6),
       (3, 1), (3, 2), (3, 6), (3, 7), (4, 1), (4, 3), 
       (4, 7), (4, 8), (4, 9);