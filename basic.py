import json
import requests
python_data = {'name': "Ishwar", "data": 22, "is_valid": True}

json_data = json.dumps(python_data)
#print(json_data)
#{"name": "Ishwar", "data": 22, "is_valid": true} (JSON Have Double quotes)

python_data2 = json.loads(json_data)

#print(python_data2 == python_data)  #true
url = 'http://127.0.0.1:8000/studentcreate/'

def test():
    
    #r = requests.get(url = url)
    #print(r)
    #data = r.json()
    #print(data)


    data = {
        'name': 'Ankit',
        'roll':4,
        'city':'Lakhisarai'
    }
    json_data = json.dumps(data)
    r = requests.post(url = url, data=json_data)
    print(r.json())





def get_data(id):
    data ={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = url, data=json_data)
    data = r.json()
    print(data)