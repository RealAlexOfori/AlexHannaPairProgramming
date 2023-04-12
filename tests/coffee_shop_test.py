import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("Beanz", 500, "Hot Chocolate")
        self.customer = Customer("Hanna", 300)

    def test_has_name(self):
        self.assertEqual("Beanz", self.coffee_shop.name)

    def test_till_has_money(self):
        self.assertEqual( 500, self.coffee_shop.till)

    # def test_sell_drink_to_customer(self):
    #     drink1 = Drink("Hot Chocolate", 4.00)
    #     customer1 = Customer("Hanna", 300)
    #     #function from coffee_shop to sell a specific drink to a specific customer
    #     self.coffee_shop.sell_drink_to_customer(drink1, customer1)
    #     self

    #     #checking if customer wallet has been reduced
    #     #checking if till has been increased

    def test_reduce_cash(self):
        self.customer.reduce_cash(4)
        self.assertEqual(296, self.customer.wallet)

    def test_increase_cash_in_till(self):
        self.coffee_shop.increase_cash_in_till(4)
        self.assertEqual(504, self.coffee_shop.till)

    # def check_age_before_serving(self, age):
    #     self.coffee_shop.check_age(age >16)
    #     self.assertEqual(18, self.coffee_shop.age)