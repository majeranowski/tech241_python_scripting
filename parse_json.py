# Working with JSON in Python
# JavaScript Object Notation (JSON)

# high level human readable language - mostyle used to transport data.

# JSON works with key/value pairs

# {"firstname": "John", "lastname": "Bond"}

# parsing? Turning a string into a data structure and vice versa

import json # importing json library
#
# json = json.loads(open('example.json').read()) # save json file to a python dict
# value = json['name']  # gettin the value of 'name' key
# for key in json:
#     print(key)

# more advanced:
# script to make an absolute of the JSON file
import os
script_dir = os.path.dirname(__file__)
print("The script is located at: " + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json')
print("The script absolute path is: " + script_absolute_path)

# script to parse JSON
json =json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

# loop through the JSON:

for key in json:
    value = json[key]
    print("The key and value are {} = {}".format(key, value))