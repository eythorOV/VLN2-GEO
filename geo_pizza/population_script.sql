--menu
INSERT INTO menu_toppings (name, price)
VALUES ('Sauce', 345), ('Cheese', 345), ('Vegan Cheese', 475), ('Basil', 0),
    ('White Sauce',0), ('Ham', 475), ('Pineapple', 345), ('Pepperoni', 475),
    ('Mushrooms', 345), ('Broccoli', 345), ('Calabresa', 475), ('Onion', 345),
    ('Black Olives', 345), ('Origano', 0), ('Green Olives', 345), ('Salami', 475),
    ('Bacon', 475), ('Chili Pepper', 0), ('Teriyaki Chicken', 475), ('Seaweed', 345),
    ('Mayonnaise', 0), ('Shrimp', 475), ('Chili peppers', 345), ('Lime Leaves', 0),
    ('Capsicum', 345), ('Paprika', 345), ('Candy Corn', 345), ('Jelly Beans', 345), ('Gummy Bears', 345),
    ('Sprinkles' , 345), ('Peppers', 345), ('Garlic', 345), ('Basil', 345), ('Oregano', 345),
    ('Vegan Chicken', 475), ('Spinach', 345), ('Vegan Chicken', 475);


INSERT INTO menu_pizza (name, price, spicy, vegan, desert, popular, image, description, longDescription)
VALUES
('Margherita Pizza', 1990, false, false, false, true, 'https://lh3.googleusercontent.com/hCkVD9BFiQIBip8BE4pHIGzC55METWn7ZGdbh_Sghs9RfjcJqxs9dUvMne04vlMrLdk4ndnpsaHm4vusplPEinckFPkYyd-2G8APIQA9i0jDi_SyQW6IqQ=s0', 'Fresh tomatoes and basil on our classic cheese pizza', 'Our Margherita Pizza is a classic favorite. Topped with fresh tomatoes and basil, and baked to perfection on our signature thin crust.'),
('Pepperoni Pizza', 2590, true, false, false, true, 'https://lh3.googleusercontent.com/PPTRiVuarSllx4QvsSqBs92fmMpe8FaV5UaPc2uPVcADOK9q8rmY5E-gBpbim6d-CT29v8T1oqduy0Gygfes_9TZOdscLcKAePaPxM9_2Vj8AgO4q9zgtZA=s0', 'The classic pizza with spicy pepperoni', 'Our Pepperoni Pizza is a crowd-pleaser! Made with spicy pepperoni and our signature tomato sauce, this pizza is perfect for those who like a little kick.'),
('White Pizza', 2790, false, false, false, true, 'https://lh3.googleusercontent.com/QB9CDcHeihwJs_meHOqp3fzpDBtMZMLEFdKidF6TBvrJfJaVNZkxEM18aEzFukxvttHlzVnd1hYWQxKCAP0FA4NE6neEy0CkXeYYm4CZwTTI8nzClZJt=s0', 'Mushrooms and broccoli on a white sauce base', 'Our White Pizza is a delicious twist on the classic tomato sauce-based pizza. Made with a creamy white sauce and topped with mushrooms and broccoli, it is a favorite among vegetarians.'),
('Calabresa Pizza', 2990, true, false, false, false, 'https://lh3.googleusercontent.com/bcglFbkfE0v0PIYt8fcv5wQXSkDqLL1sPacNFYRoTkn3AduDBT4IeCqnIImrmklwn9_pZDqqdTvimvZtFtZoawvovlSE9MX8AxPSnyeWqtU0SqrrOYlB8g=s0', 'Spicy calabresa sausage, onion rings, and whole black olives', 'Our Calabresa Pizza is not for the faint of heart! Made with spicy calabresa sausage, onion rings, and whole black olives, this pizza is sure to satisfy your cravings for something spicy.'),
('Muzzarella Pizza', 2390, false, false, false, false, 'https://lh3.googleusercontent.com/KUd_rod9Mt5wDuLyioL0RP_0P5ZlJYwLV_ujPYF76GEVwHck56sgb-l9qgDOBg6-wpohvClXHY5IDXFqkjw1d0S-zQdSw4fBK0r3ex-miF5rw_gWeX2T7w=s0', 'Oregano and whole green olives on our classic cheese pizza', 'Our Muzzarella Pizza is a simple yet delicious pizza that everyone will love! Made with our classic cheese pizza and topped with oregano and whole green olives, it is the perfect choice for those who prefer a more traditional pizza.'),
('Hawaiian Pizza', 2890, false, false, false, true, 'https://lh3.googleusercontent.com/b2vyRukzZN59IGTCAKjAysdNDjpgUFqFH7h6wUh7Sgpi1APHRO13aHIKJfHmIFO3Fn5RDdYhPpk1ExjDARRhqFMQHmGnw9BOKXWxSa1tSALSwmd44lQ2Jg=s0', 'Ham and pineapple on our classic cheese pizza', 'Our Hawaiian Pizza is a sweet and savory treat! Made with ham and pineapple on our classic cheese pizza, it is the perfect choice for those who like a little bit of both.'),
('Magyaros Pizza', 3190, true, false, false, false, 'https://lh3.googleusercontent.com/SRYODF8wPNozz_a2J521Dvu2nZdqgsAVa4wDZSq1QZa8q_b61GQ1IqPd6-A_94IJbpnqiHG0MUWglufLgKmji8hNaHwNB9qQLWTBpCT7LgVdCwh7o44sGo0=s0', 'Spicy salami, bacon, onion, and chili pepper', 'Our Magyaros Pizza is a spicy and savory delight! Made with spicy salami, bacon, onion, and chili pepper, it is the perfect choice for those who like their pizza with a little bit of heat.'),
('Teriyaki Mayonnaise Pizza', 3390, false, false, false, false, 'https://lh3.googleusercontent.com/tueBfyTsUozBolfEznOOMq-0dSp0PAlbQDpDVD_SskeJXObvny7AJ8XbDum3SxBJlqThw-cCR4H8fFmfQZkOWUMLDoL2qPq-tpeQwOHhRwNDSq8Y06DvIg=s0', 'Teriyaki chicken, seaweed, and mayonnaise', 'Our Teriyaki Mayonnaise Pizza is a unique and delicious pizza that you wont find anywhere else! Made with teriyaki chicken, seaweed, and mayonnaise, it is the perfect choice for those who like to try something new.'),
('Tom Yum Pizza', 3490, true, false, false, false, 'https://lh3.googleusercontent.com/FVUg0W-UjIyXLBzxQxZfbAQeRCuhGJFMs0E2MtiD4G5xYpOpkqm-ZNCfqWRnyINU7rVgxyvubUiEW-6y9QBNKmjCgbP15nWMulePIVVjQmEjElc4ThDJHQ=s0', 'Shrimp, mushrooms, chili peppers, and lime leaves', 'Our Tom Yum Pizza is a fusion of Thai and Italian flavors! Made with shrimp, mushrooms, chili peppers, and lime leaves, it is the perfect choice for those who like their pizza with a little bit of spice.'),
('Vegan Feast', 3590, false, true, false, false, 'https://lh3.googleusercontent.com/XU-n0dJajzqLJXqBpFkQKamPeALAuw8fy3vKvyhvXHklkoXJ7cHeT0OaAEVJA3DPZUBAnPWJeMxLw28niOAhTtpcOVLLX00nZJOz_CuXPa0RpADBasO7Ow=s0', 'Vegan cheese, vegan chicken, capsicum, onion, and paprika', 'A vegan delight, loaded with vegan cheese, vegan chicken, capsicum, onion, and paprika, baked to perfection.'),
('Dessert Pizza', 3990, false, false, true, false, 'https://lh3.googleusercontent.com/CfXmWdMUN_ztAcOFqb3nIyR8IfIALSeRB79-3k8JDfKxOHaBNOnEawESSgTfqIyphO_7nPVOLd9E4P2WGiOQJLrwDecx6UG5QdGhQtondJgHhZSC6mVTZ_g=s0', 'Candy corn, jelly beans, gummy bears, and sprinkles', 'A sweet dessert pizza loaded with candy corn, jelly beans, gummy bears, and sprinkles, baked to perfection.');

INSERT INTO menu_pizza_toppings (pizza_id, toppings_id)
VALUES
-- Margherita Pizza
(1, 1), (1, 2), (1, 7),
-- Pepperoni Pizza
(2, 1), (2, 2), (2, 8),
-- White Pizza
(3, 1), (3, 2), (3, 5), (3, 9), (3, 10),
-- Calabresa Pizza
(4, 1), (4, 2), (4, 11), (4, 12),
-- Muzzarella Pizza
(5, 1), (5, 2), (5, 6), (5, 15),
-- Hawaiian Pizza
(6, 1), (6, 2), (6, 6), (6, 7),
-- Magyaros Pizza
(7, 1), (7, 2), (7, 11), (7, 13), (7, 24),
-- Teriyaki Mayonnaise Pizza
(8, 1), (8, 2), (8, 21), (8, 22), (8, 23),
-- Tom Yum Pizza
(9, 1), (9, 2), (9, 8), (9, 12), (9, 20), (9, 25),
-- Vegan Feast
(10, 1), (10, 3), (10, 12), (10, 26), (10, 27),
-- Dessert Pizza
(11, 28), (11, 29), (11, 30), (11, 31);

--offers
INSERT INTO offers_sodas (name, image)
VALUES ('Coca Cola','https://cdn-icons-png.flaticon.com/512/3076/3076028.png'), ('Cola light', 'https://cdn-icons-png.flaticon.com/512/9074/9074709.png'), ('Sparkling water', 'https://cdn-icons-png.flaticon.com/512/859/859301.png'), ('Orange Soda', 'https://cdn-icons-png.flaticon.com/512/6854/6854143.png'), ('7up', 'https://cdn-icons-png.flaticon.com/512/4507/4507457.png');

INSERT INTO offers_breadsticks (name, image)
VALUES ('classic breadsticks', 'https://cdn-icons-png.flaticon.com/512/5221/5221865.png'), ('vegan breadsticks', 'https://cdn-icons-png.flaticon.com/512/5221/5221865.png');

INSERT INTO offers_specialoffer (name, description, price, image)
VALUES ('Special Offer', 'Pizza, breadsticks, and soda - great value, great taste.', 2990, 'https://i.ibb.co/HKjn1zt/Special-offer.png');

INSERT offers_lunchoffer (name, description, price, image)
VALUES ('Lunch Offer', 'Pizza and soda - quick and tasty.', 2490, 'https://i.ibb.co/tbVM1jd/Lunch-offer.png');

INSERT INTO offers_TwoForOne (name, description, price, image)
VALUES ('Two for One', 'Get 2 delicious pizzas and 1 refreshing soda for the price of 1 pizza', 3990, 'https://i.ibb.co/4SNhHp0/2-for-1.png');

--chat offers
INSERT INTO offers_sodas (name, image)
VALUES ('Coca Cola','https://cdn-icons-png.flaticon.com/512/3076/3076028.png'), ('Cola light', 'https://cdn-icons-png.flaticon.com/512/9074/9074709.png'), ('Sparkling water', 'https://cdn-icons-png.flaticon.com/512/859/859301.png'), ('Orange Soda', 'https://cdn-icons-png.flaticon.com/512/6854/6854143.png'), ('7up', 'https://cdn-icons-png.flaticon.com/512/4507/4507457.png');

INSERT INTO offers_breadsticks (name, image)
VALUES ('classic breadsticks', 'https://cdn-icons-png.flaticon.com/512/5221/5221865.png'), ('vegan breadsticks', 'https://cdn-icons-png.flaticon.com/512/5221/5221865.png');

INSERT INTO offers_specialoffer (name, description, price, image, pizzas_id, soda_id, breadsticks_id)
VALUES ('Special Offer', 'Pizza, breadsticks, and soda - great value, great taste.', 2990, 'https://i.ibb.co/HKjn1zt/Special-offer.png', NULL, 1, 1);

INSERT INTO offers_lunchoffer (name, description, price, image, pizzas_id, soda_id)
VALUES ('Lunch Offer', 'Pizza and soda - quick and tasty.', 2490, 'https://i.ibb.co/tbVM1jd/Lunch-offer.png', NULL, 1);

INSERT INTO offers_twoforone (name, description, price, image, soda_id, breadsticks_id)
VALUES ('Two for One', 'Get 2 delicious pizzas and 1 refreshing soda for the price of 1 pizza', 3990, 'https://i.ibb.co/4SNhHp0/2-for-1.png', 1, 1);