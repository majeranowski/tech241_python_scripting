# SCRIPTING IN PYTHON

### Lesson:

scripting - 1 file - simple  / easy to read / very specific / high level languages
programming - many files - complex / flexible / low level languages

high level language - easier to read

low level language - very technical, computer level

scripting scope is targeted for one specific task

why we write scripts in python?
* python is easy
* a lot of libraries
* language Interoperability - works good with different software 
* large community / open source


Photoshop analogy:
resizing image - a lot of steps to do in photoshop

instead of manually changing resolution for 100 images. just write a script 


Why Devops care about scripting:

* Automation 
* Configuration -> IaC (configuration scripts, orchestration)
* making things more efficient

### Research:


In Python, scripting refers to the process of writing scripts or programs that automate specific tasks or perform a series of instructions. A script is a file containing a sequence of Python statements that can be executed by an interpreter.

Scripting in Python is often used for various purposes, such as:

* Task Automation: Python scripts can be written to automate repetitive tasks, such as file operations, data processing, system administration, web scraping, or interacting with APIs. By writing scripts, you can save time and effort by automating these tasks and making them more efficient.

* Prototyping: Python is a popular language for rapid prototyping of software applications. It allows developers to quickly write scripts to test ideas, algorithms, or proof-of-concept implementations. Python's simplicity and readability make it easy to express ideas and experiment with different approaches.

* System Administration: Python is widely used in system administration tasks, such as managing and configuring servers, automating backups, monitoring network resources, or performing system maintenance. Scripts can be written to handle these tasks and ensure smooth operations of computer systems.

* Data Analysis and Manipulation: Python provides powerful libraries and tools for data analysis and manipulation, such as NumPy, Pandas, and matplotlib. Scripts can be written to read, process, transform, analyze, and visualize data, making Python a popular choice for data scientists and analysts.

* Web Development: Python is used for server-side web development, where scripts are written to handle HTTP requests, process data, generate dynamic web content, interact with databases, and build web applications using frameworks like Django or Flask.

Python's simplicity, versatility, and vast ecosystem of libraries make it well-suited for scripting tasks. It allows developers to write scripts that are readable, concise, and easy to maintain. Additionally, Python's cross-platform support enables scripts to be executed on different operating systems without major modifications, providing portability and flexibility.

### SCRIPTING IN DEVOPS

Scripting is beneficial for DevOps (Development and Operations) practices due to the following reasons:

* Automation: DevOps aims to automate manual tasks and streamline processes. Scripting allows for the automation of repetitive and time-consuming tasks such as provisioning infrastructure, configuring systems, deploying applications, and managing environments. By writing scripts, DevOps engineers can automate these tasks, saving time and reducing the chance of human error.

* Infrastructure as Code (IaC): In DevOps, infrastructure is often treated as code through IaC practices. Scripts can be written using tools like Ansible, Puppet, or Terraform to define and manage infrastructure configurations. Infrastructure can be easily provisioned, configured, and version-controlled using scripts, providing consistency and reproducibility across different environments.

* Continuous Integration and Continuous Deployment (CI/CD): Scripting plays a crucial role in implementing CI/CD pipelines. Build scripts can be created to compile, test, and package applications, while deployment scripts can automate the process of deploying applications to different environments. By using scripts, DevOps teams can ensure that the CI/CD pipeline is efficient, reliable, and scalable.

* Configuration Management: Configuration management is a fundamental aspect of DevOps. Scripts can be used to define and manage configuration settings for different systems and environments. Configuration scripts can enforce consistency, manage dependencies, and ensure that systems are properly configured and aligned with desired states.

* Troubleshooting and Debugging: Scripts can assist in troubleshooting and debugging issues in the DevOps environment. By writing diagnostic scripts, DevOps engineers can collect relevant system information, check logs, run tests, and perform analysis to identify and resolve problems more efficiently.

* Collaboration and Knowledge Sharing: Scripts provide a common language and a reusable form of automation. DevOps teams can collaborate by sharing scripts, templates, and code snippets, fostering knowledge sharing and facilitating consistent practices across the team. Scripts can be version-controlled, documented, and shared within the organization, promoting collaboration and improving team productivity.

Overall, scripting in DevOps enables automation, consistency, scalability, and efficiency in the development and operations processes. It allows DevOps teams to focus on higher-level tasks, reduces manual errors, enhances productivity, and promotes collaboration and best practices within the team.

### Example of scripting in Python
Here is a complete example script where we use JSON and os python module to retrieve the absolute path of the JSON file. Also, we are using for loop to print all the keys and values of the JSON file.

```python
import json
import os

# Script to create absolute path of the JSON file.

script_dir = os.path.dirname(__file__)
print("The Script is located at:" + script_dir )
script_absolute_path = os.path.join(script_dir, 'example.json')
print("The Script Path is:" + script_absolute_path)

# Script to parse JSON

json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

# Loop through JSON keys and values

for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))
```

### Very useful scripts:

How to check if JSON is valid:

```python
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
```

run script in terminal:

`py <name of the python file> <json file name>`


### JSON

```python
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
```

### Parsing remote JSON

```python
import urllib.request
import json

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data)

```

### Converting JSON file to YAML:

```python
import json
import os
import sys
import yaml
# checking there is a file named  passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    #failing if the file is not found
    else:
        print("Error")
        exit(1)
# no file no usage
else:
    print("You are not using this program properly")
# processing the conversion
output = yaml.dump(source_content)

# if no target file send to stdout
if len(sys.argv) < 3:
    print(output)
 # if the target file already exist
elif os.path.exists(sys.argv[2]):
    print("Error, file already exists")
    exit(1)
 # otherwise write to the specific target
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()
```

run the script in terminal:
`py <python file with script> <input file with JSON> <output YAML file we want to create>`

### YAML to JSON

```python
import json
import os
import sys
import yaml
# checking there is a file named  passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    #failing if the file is not found
    else:
        print("Error")
        exit(1)
# no file no usage
else:
    print("You are not using this program properly")
# processing the conversion
output = json.dumps(source_content)

# if no target file send to stdout
if len(sys.argv) < 3:
    print(output)
 # if the target file already exist
elif os.path.exists(sys.argv[2]):
    print("Error, file already exists")
    exit(1)
 # otherwise write to the specific target
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()
```

run the script in terminal:
`py <python file with script> <input file with YAML> <output JSON file we want to create>`
