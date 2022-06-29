class Customer:
    def __init__(self, _name, _wallet, _age, _drunkeness):
        self.name = _name,
        self.wallet = _wallet
        self.age = _age
        self.drunkeness_level = _drunkeness

    def buy_drink(self, pub, drink):
        if self.age >= 18 and self.drunkeness_level <= 15:
            pub.till += drink.price
            self.wallet -= drink.price
            self.drunkeness_level += drink.alcohol_level
            pub.stock[drink]-=1

    def buy_food(self, pub, food):
        pub.till += food.price
        self.wallet -= food.price
        self.drunkeness_level -= food.rejuvenation
