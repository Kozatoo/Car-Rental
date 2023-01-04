import json
import os
from DataImporter import importData
from PriceCalculator import CalculatePrice
from Models.Commission import Commission

script_dir = os.path.dirname(__file__) 
rel_path = "data/input.json"
f = open(os.path.join(script_dir, rel_path))

data = json.load(f)
cars , rentals = importData(data)

final_rentals = []
for id, rental in  rentals.items():
    try:
        rented_car = cars[rental.car_id]
        km_price = rental.distance * rented_car.price_per_km
        
        rental_duration = rental.rentalDuration()
        duration_price = CalculatePrice(rental_duration, rented_car.price_per_day)       
            
        price = km_price + duration_price
        commission = Commission(price, rental_duration)
        final_rentals.append({ "id" : id, "price" : price, "commission" : commission.to_json() })
        
    except KeyError:
        print(f"no car with the id {rental.car_id} exists")
    # except TypeError:
    #     print("There must be a problem in the input file")

output_rel_path = "data/output.json"
with open(os.path.join(script_dir, output_rel_path),"w") as outfile: 
    json.dump( {"rentals": final_rentals},outfile,indent=2)