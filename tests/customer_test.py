import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink 

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Hanna", 300)

    def test_customer_has_name(self):
        self.assertEqual("Hanna", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(300, self.customer.wallet)

    # def test_customer_can_buy_drink(self):
