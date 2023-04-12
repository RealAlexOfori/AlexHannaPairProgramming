class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def drinks_list(self):
        return len(self.drinks)

    def increase_cash_in_till(self, money_added):
        self.till += money_added

    def sell_drink(self,customer,drink):
        customer.reduce_cash(drink.price)
        self.increase_cash_in_till(drink.price)
        
    # def check_age(self, age):
    #     if self.age > 16:

        