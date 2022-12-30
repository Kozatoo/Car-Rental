from typing import Dict, Tuple
from Models.Car import Car
from Models.Rental import Rental

def importCars(data) -> Dict[int, Car]:
    cars = dict()
    for car in data:
        try:
            cars[car["id"]] = Car(car["price_per_day"],car["price_per_km"])
        except KeyError:
            print(f"Invalid data with this input: {car}")
        except Exception:
            print(f"Car not added - {car}")
    return cars

def importRentals(data) -> Dict[int, Rental]: 
    rentals = dict()
    for rental in data:
        try:
            rentals[rental["id"]] = Rental(rental["car_id"], rental["start_date"], rental["end_date"], rental["distance"])
        except KeyError:
            print(f"Invalid data with this input: {rental}")
        except Exception:
            print(f"Rental not added - {rental}")
    return rentals

def importData(data) -> Tuple[Dict[int, Car], Dict[int, Rental]]:
    return importCars(data["cars"]), importRentals(data["rentals"])