#!/usr/bin/python3
"""
JSON as object
"""

import json


def save_to_json_file(my_obj, filename):
    'JSON as object'
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
