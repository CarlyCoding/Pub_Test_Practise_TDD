import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("The Bannermans", 200.00)
        self.drink = Drink("Tennant", 3.00, 5)
        self.customer = Customer("Sideshow Bob", 20.00, 40)


    def test_pub_has_name(self):
        self.assertEqual( "The Prancing Pony", self.pub.name )
    
    def test_drink_has_price(self):
        self.assertAlmostEqual( 3.00, self.drink.price)
    
    # def test_buy_drink(self):
    #     # self.pub.add_drink(self.drink)
    #     self.customer.buy_drink(self.pub, self.drink)
    #     self.assertEqual(103.00, self.pub.till)
    #     self.assertEqual(17.00, self.customer.wallet)

    def test_refused_service(self):
        self.assertEqual(20.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)