import json

with open("relations.json", "r") as file:
    loaded_dict = json.load(file)

for rel in loaded_dict["Item 1A"]:
    print (rel , "/n")

#merge relations 
