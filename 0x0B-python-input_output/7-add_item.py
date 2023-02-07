#!/usr/bin/python3
"""
Module 9-add-item

Contains function which adds and saves Python obj to a json file; load objexts

# run with ./7-add_item.py
#
# cat add_item.json ; echo ""
# expect output: []
#
# ./9-add_item.py some random args
# cat add_item.json ; echo ""
# expect output: ["some", "random", "args"]
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_content = load_from_json_file(filename)
except FileNOtFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], filename)
