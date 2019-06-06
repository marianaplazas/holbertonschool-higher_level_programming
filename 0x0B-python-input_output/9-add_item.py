#!/usr/bin/python3
"""
add all arguments
"""

import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


#def load_add_save(filename, args):
    'add all arguments'
    try:
        new_json_object = load_from_json_file(filename)
    except FileNotFoundError:
        new_json_object = []
    new_json_object = save_to_json_file(new_json_object + args, filename)

if __name__ == "__main__":
    filename = "add_item.json"
    load_add_save(filename, sys.argv[1:])
