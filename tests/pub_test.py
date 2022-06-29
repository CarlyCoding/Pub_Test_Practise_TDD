import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.pub1 = Pub("The Bannermans", 200)
        self.drink = Drink("Tennants", 3, 5)
        self.drink2 = Drink("Strongbow", 4, 4)
        self.customer = Customer("Sideshow Bob", 20, 40, 10)
        self.food = Food("Pot Noodle", 2, 5)
        self.pub.stock = {
            self.drink : 10,
            self.drink2 : 5}
       


    def test_pub_has_name(self):
        self.assertEqual( "The Prancing Pony", self.pub.name )
    
    def test_food_rejuvention(self):
        self.customer.buy_food(self.pub, self.food)
        self.customer.buy_drink(self.pub, self.drink)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(15, self.customer.wallet)

    def test_drink_has_price(self):
        self.assertAlmostEqual( 3, self.drink.price)


    def test_buy_drink(self):
        self.customer.buy_drink(self.pub, self.drink)
        self.assertEqual(103, self.pub.till)
        self.assertEqual(17, self.customer.wallet)
        self.assertEqual(9, self.pub.stock[self.drink])
    

    def test_stock_value(self):
        self.assertEqual(50, self.pub.check_stock_value())

    # def test_refused_service(self):
    #     self.assertEqual(20.00, self.customer.wallet)
    #     self.assertEqual(100.00, self.pub.till)