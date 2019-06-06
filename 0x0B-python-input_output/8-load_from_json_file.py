#!/usr/bin/python3
"""
fom JSNO object
"""

import json


def load_from_json_file(filename):
    'JSNO object'
    with open(filename) as f:
        return (json.load(f))
