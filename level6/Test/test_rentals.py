import unittest
from Models.rental import Rental
from Models.car import Car

class testRentalsDuration(unittest.TestCase):
    def test_positive_Duration(self):
        car = Car(50,50)
        rental = Rental("1",car,"2015-12-8","2015-12-9", 500)
        assert rental.rentalDuration() == 2
      
    def test_one_day_duration(self):
        car = Car(50,50)
        rental = Rental("1",car,"2015-12-8","2015-12-8", 500)
        assert rental.rentalDuration() == 1
        
    def test_negative_Duration(self):
        car = Car(50,50)
        rental = Rental("1",car,"2015-12-10","2015-12-9", 500)
        assert rental.rentalDuration() == 0
    
class TestRentalPrices(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(2000,10)
        self.rental = Rental(1, self.car, "2015-12-8", "2015-12-8", 100 )   
    def test_CalculatePrice(self):
        #Testing duration price
        assert self.rental.CalculateDurationPrice(2000) == 2000
        
        #Testing commissions
        assert self.rental.price == 3000
        assert self.rental.commission.commissioned_part == 900
        assert self.rental.commission.assistance_fee == 100
        assert self.rental.commission.insurance_fee == 450
        assert self.rental.commission.drivy_fee == 350
        
    def test_setInvoice(self):
        print(self.rental.invoices)
        assert self.rental.invoices != []
        
    def test_setInvoiceWithNoPrice(self):
        self.rental.price = None
        self.assertRaises(Exception, self.rental.setInvoices)
        
    def test_setInvoiceWithNoCommission(self):
        self.rental.commission = None
        self.assertRaises(Exception, self.rental.setInvoices)
    
    def test_toJson(self):
        # assert self.rental.to_json() 
        excepted_json = {
                            "id":1,
                            "actions":[
                                {
                                    "who":"driver",
                                    "type":"debit",
                                    "amount":3000
                                },
                                {
                                    "who":"owner",
                                    "type":"credit",
                                    "amount":2100
                                },
                                {
                                    "who":"insurance",
                                    "type":"credit",
                                    "amount":450
                                },
                                {
                                    "who":"assistance",
                                    "type":"credit",
                                    "amount":100
                                },
                                {
                                    "who":"drivy",
                                    "type":"credit",
                                    "amount":350
                                }
                            ]
                            }
        assert excepted_json == self.rental.to_json()
        

if __name__ == '__main__':
    unittest.main()
