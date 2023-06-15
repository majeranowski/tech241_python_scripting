# Basics of scripting in Python

# Libraries and Modules - Module is a collection of functions / Library is a collection of modules (much bigger than modules)

# Seven "core" modules in Python:

# # 1) sys
#
# import sys
#
# #Get Python version
# print(sys.version)
#
# # 2) os
#
# import os
#
# #Get current working directory
# print(os.getcwd())
#
# # 3) subprocess
#
# import subprocess
#
# #run external file when executed
# subprocess.run(["python", "hello_world.py"])
#
# # 4) math
#
# import math
#
# pi = math.pi
# pi_string = str(pi)
# print("The value of pi is", pi_string)

# 5) random
#
# import random
# # get random number from the range
# randum = random.randrange(1, 10)
# print(randum)

# 6) datetime

# import datetime
#
# what_is_the_date = datetime.datetime.now()
#
# print(what_is_the_date.month)

# 7) json

# import json
#
# x = {
#     "name": "john",
#     "age": 30,
#     "city": "London"
# }
#
# y = json.dumps(x)
#
# print(type(y))