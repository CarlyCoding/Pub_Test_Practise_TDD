class Pub:
    
    # Constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.stock = {}
    
    def check_stock_value(self):
        total = 0
        stock = self.stock.keys()
        for drink in stock:
            total += (drink.price * self.stock[drink])
        return total