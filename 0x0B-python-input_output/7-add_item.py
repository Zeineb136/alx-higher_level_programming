#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

try:
    list_python = load_from_json_file("add_item.json")
except:
    list_python = []

for i in argv[1:]:
    list_python.append("i")

save_to_json_file(list_python, "add_item.json")
