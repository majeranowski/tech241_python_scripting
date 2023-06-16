import os
import json
import sys

# How to check if the JSON is valid

if len(sys.argv) > 1:  # if there are more than 1 arguments in termina
    if os.path.exists(sys.argv[1]):  #if the file axtually exists
        file = open(sys.argv[1], "r")
        json.load(file)   #check if it is JSON, if it opens
        file.close()   # you have to close if u opened
        print("JSON is VALID!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: check_json.py <file>")