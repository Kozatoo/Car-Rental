from datetime import datetime
from typing import List
from Models.Car import Car
from Models.Invoice import *
from Models.Commission import Commission

sales =  [
    {
        "day": 1,
        "decrease" : 10
    },
    {
        "day": 4,
        "decrease" : 30
    },
    {
        "day": 10,
        "decrease" : 50
    }    
]

class Rental:
    def __init__(self, id: int, car_id: int , start_date: str, end_date: str, distance: int) -> None:
        self.id = id
        self.car_id = car_id
        date_format ="%Y-%m-%d"
        try:
            self.start_date = datetime.strptime(start_date, date_format)
            self.end_date = datetime.strptime(end_date, date_format)
        except ValueError:
            print(f"Invalid data format: {end_date, start_date} ")
            raise Exception
        self.distance = distance

    def rentalDuration(self) -> int :
        if(self.duration == None):
            self.duration =(self.end_date-self.start_date).days + 1
        return self.duration
        
    def CalculateDurationPrice(self, price_per_day : int) -> int :
        # We assume that the first day  always costs the original price
        total_price = price_per_day
        for index, sale in enumerate(sales):
            counted_days = 0
            if index == len(sales) - 1 or self.rentalDuration() < sales[index + 1 ]["day"] :
                counted_days = self.rentalDuration() - sale["day"] if self.rentalDuration() > sale["day"] else 0
            else: 
                counted_days = sales[index + 1 ]["day"] - sale["day"] 

            total_price += ( counted_days * price_per_day *  ( 100 - sale["decrease"]) )// 100 
        return total_price
    
    def CalculatePrice(self, car: Car ) -> None: 
        km_price = self.distance * car.price_per_km
        duration_price = self.CalculateDurationPrice(car.price_per_day)       
            
        self.price = km_price + duration_price
        self.commission = Commission(self.price, self.rentalDuration())
    
    def setInvoices(self):
        if self.commission == None :
            print(f"Commission list is needed but empty for rental {self.id}")
            raise Exception
        if self.price == None : 
            print(f"Commission price is needed but empty for rental {self.id}")
            raise Exception
        self.invoices = Invoice.getRentalInvoices(self)        
    
    def to_json(self)-> dict:
        # return { "id" : self.id,
        #          "price" : self.price,
        #          "commission" : self.commission.to_json() }  
        return { "id" : self.id, "actions": Invoice.list_to_json(self.invoices)}
        
            
    id: int
    car_id: int 
    start_date: datetime
    end_date: datetime
    distance: int
    duration: int = None
    price = None
    commission: Commission = None
    invoices: List[Invoice] = None

