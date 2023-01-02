import json
import os
from DataImporter import importData
from Models.Commission import Commission

script_dir = os.path.dirname(__file__) 
rel_path = "data/input.json"
f = open(os.path.join(script_dir, rel_path))

data = json.load(f)
cars , rentals = importData(data)

final_rentals = []
for rental in rentals:
    try:
        rented_car = cars[rental.car_id]
        rental.CalculatePrice(rented_car)
        rental.setInvoices()
        final_rentals.append(rental.to_json())
        
    except KeyError:
        print(f"no car with the id {rental.car_id} exists")

output_rel_path = "data/output.json"
with open(os.path.join(script_dir, output_rel_path),"w") as outfile: 
    json.dump( {"rentals": final_rentals},outfile,indent=2)