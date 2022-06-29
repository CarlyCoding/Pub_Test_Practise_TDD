class Pub:
    
    # Constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.drinks = []
    
    def add_drink(self, drink):
        self.drinks.append(drink)