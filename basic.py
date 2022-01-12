import json
python_data = {'name': "Ishwar", "data": 22, "is_valid": True}

json_data = json.dumps(python_data)
print(json_data)
#{"name": "Ishwar", "data": 22, "is_valid": true} (JSON Have Double quotes)

python_data2 = json.loads(json_data)

print(python_data2 == python_data)  #true


 