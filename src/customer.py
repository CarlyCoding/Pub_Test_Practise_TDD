class Customer:
    def __init__(self, _name, _wallet, _age):
        self.name = _name,
        self.wallet = _wallet
        self.age = _age
        self.drunkeness_level = 15

    def buy_drink(self, pub, drink):
        if self.age >= 18 and self.drunkeness_level <= 14:
            pub.till += drink.price
            self.wallet -= drink.price
            self.drunkeness_level += drink.alochol_level
