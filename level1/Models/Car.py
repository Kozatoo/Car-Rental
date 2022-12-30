class Car:
    id:int
    price_per_day: int
    price_per_km: int 
    def __init__(self, price_per_day: int, price_per_km: int):
        self.price_per_day = price_per_day
        self.price_per_km = price_per_km