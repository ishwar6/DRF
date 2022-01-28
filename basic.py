import time
import threading
from threading import Thread
import json
import requests
python_data = {'name': "Ishwar", "data": 22, "is_valid": True}

json_data = json.dumps(python_data)
# print(json_data)
# {"name": "Ishwar", "data": 22, "is_valid": true} (JSON Have Double quotes)

python_data2 = json.loads(json_data)

# print(python_data2 == python_data)  #true
url = 'http://127.0.0.1:8000/studentcreate/'


def test():

    #r = requests.get(url = url)
    # print(r)
    #data = r.json()
    # print(data)

    data = {
        'name': 'Ankit',
        'roll': 4,
        'city': 'Lakhisarai'
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    print(r.json())


def get_data(id):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)


def display():
    for i in range(4):
        print("Child thread")


t = Thread(target=display)
t.start()

for i in range(3):
    print("Main Thread")


def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())


thread_delay('a', 4)


def volume_cube(a):
    print("Volume of Cube:", a*a*a)


def volume_square(a):
    print("Volume of Square:", a*a)


t1 = threading.Thread(target=volume_cube, args=(2))
t2 = threading.Thread(target=volume_square, args=(3))
