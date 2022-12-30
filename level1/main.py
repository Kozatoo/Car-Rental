import json
from DataImporter import importData

f = open("./data/input.json")

data = json.load(f)
cars , rentals = importData(data)

final_rentals = []
for id, rental in  rentals.items():
    try:
        rented_car = cars[rental.car_id]
        price = rental.rentalDuration() * rented_car.price_per_day + rental.distance * rented_car.price_per_km  
        
        final_rentals.append({ "id" : id, "price" : price})
    except KeyError:
        print(f"no car with the id {rental.car_id} exists")
    except TypeError:
        print("There must be a problem in the input file")

with open("./data/output.json","w") as outfile: 
    json.dump( {"rentals": final_rentals},outfile,indent=2)