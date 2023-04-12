import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Hot Chocolate", 4.00)
        self.drink2 = Drink("Coffee", 3.00)
        self.drink3 = Drink("Tea", 2.00)

    def test_drink_has_name(self):
        self.assertEqual("Hot Chocolate", self.drink1.name)

    def test_drink_has_price(self):
        self.assertEqual(4, self.drink1.price)