import unittest
from Models.rental import Rental
from Models.car import Car

class testCar(unittest.TestCase):
    
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
    
if __name__ == '__main__':
    unittest.main()
