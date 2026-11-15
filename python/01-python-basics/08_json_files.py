
========================================================================

		Lesson 40.1 — Understanding JSON in Python

========================================================================

JSON (JavaScript Object Notation) is a data format commonly used for:
- API responses.
- Cloud configuration files.
- AWS service communication.
- Infrastructure and application settings.

1. JSON vs Python dictionaries

A JSON object:

{
    "server_name": "web-01",
    "environment": "production",
    "cpu_limit": 80,
    "memory_limit": 75,
    "monitoring_enabled": true
}


Its equivalent Python dictionary:

{
     "server_name": "web-01",
     "environment": "production",
     "cpu_limit": 80,
     "memory_limit": 75,
     "monitoring_enabled": True
}




Notice two differences:

JSON	Python
true	True
false	False
null	None

JSON also uses double quotes for strings and keys.


2. Python's json module

Python provides a built-in module called json.

The most important functions are:

Function	Purpose

json.load()	Read JSON from a file
json.loads()	Parse a JSON string
json.dump()	Write JSON to a file
json.dumps()	Convert Python data into a JSON string

For now, we'll focus on json.load().


Exercise 40 — Read a JSON configuration file
Step 1: In your existing directory:

python/01-python-basics/python-modules/

Create a file called server.json containing:
{
    "server_name": "web-01",
    "environment": "production",
    "cpu_limit": 80,
    "memory_limit": 75,
    "monitoring_enabled": true
}


Step 2: In main.py, import the json module and read this file using
json.load().

Your objective:
1. Read the JSON file.
2. Store its contents in a Python variable called config.
3. Print config.
4. Print the type of config.


import json

with open("python/01-python-basics/python-modules/server.json", "r") as file:
    config2 = json.load(file)

print(config2)
print(type(config2))


Expected output
{
    'server_name': 'web-01',
    'environment': 'production',
    'cpu_limit': 80,
    'memory_limit': 75,
    'monitoring_enabled': True
}
<class 'dict'>


Important concept: json.load(file) automatically converts JSON into Python data types:
- JSON object → Python dictionary (dict)
- JSON number → Python integer (int)
- JSON boolean → Python boolean (bool)
