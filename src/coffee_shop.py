class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_cash_in_till(self, money_added):
        self.till += money_added
        
    # def check_age(self, age):
    #     if self.age > 16:

        