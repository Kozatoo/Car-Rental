from typing import Dict, Tuple, List
from Models.car import Car
from Models.rental import Rental
from Models.rentalWithOptions import RentalWithOptions
from Models.option import OptionType

def importCars(data) -> Dict[int, Car]:
    cars = dict()
    for car in data:
        try:
            if car["id"] in cars.keys():
                print(f"We already have a car with this id: {car['id']}")
                raise SystemError
            cars[car["id"]] = Car(car["price_per_day"],car["price_per_km"])
        except KeyError:
            print(f"Invalid data with this input: {car}")
        except Exception:
            print(f"Car not added - {car}")
    return cars

def importRentals(data, cars_list) -> Dict[int, Rental]: 
    rentals = {}
    for rental in data:
        try:
            if rental["id"] in rentals.keys():
                print(f"We already have a rental with this id: {rental['id']}")
                raise SystemError
            rentals[rental["id"]] = (Rental(rental["id"],cars_list[rental["car_id"]], rental["start_date"], rental["end_date"], rental["distance"]))
        except KeyError:
            print(f"Invalid data with this input: {rental}")
        except Exception:
            print(f"Rental not added - {rental}")
    return rentals

def importOptionsAndAddToRentals(data, rentals: Dict[int, Rental]) -> List[Rental]:
    options = []
    for option in data:
        rental_id = option["rental_id"]
        rental_type = OptionType.from_string(option["type"])
        if type(rentals[rental_id]) == Rental:
            rentals[rental_id] = RentalWithOptions(rentals[rental_id])
        rentals[rental_id].addOption(rental_type)
        
def importData(data) -> List[ Rental]:
    cars = importCars(data["cars"])
    rentals = importRentals(data["rentals"],cars)
    importOptionsAndAddToRentals(data["options"],rentals)
    return rentals.values()