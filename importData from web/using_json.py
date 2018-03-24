import json
# Load JSON: json_data
with open("json_3.json") as json_file:
    json_data=json.load(json_file)
print(json_data)
#Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

