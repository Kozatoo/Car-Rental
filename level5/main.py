import json
import os
from DataImporter import importData

script_dir = os.path.dirname(__file__) 
rel_path = "data/input.json"
f = open(os.path.join(script_dir, rel_path))

data = json.load(f)
rentals = importData(data)

final_rentals = []
for rental in rentals:
    try:
        final_rentals.append(rental.to_json())
        
    except KeyError:
        print(f"no car with the id {rental.car_id} exists")
    except ProcessLookupError:
        print(f"there was an error with this rental {rental}")

output_rel_path = "data/output.json"
with open(os.path.join(script_dir, output_rel_path),"w") as outfile: 
    json.dump( {"rentals": final_rentals},outfile,indent=2)