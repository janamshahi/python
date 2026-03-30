import json
data = {
    "name": "Janam",
    "age": 21,
    "course": "BITM"
}
filename = "data.json"
with open(filename, "w") as json_file:
    json.dump(data, json_file, indent=4)
print(f"Dictionary data has been stored in '{filename}'.")

