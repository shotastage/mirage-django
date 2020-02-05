"""
MIRAGE Framework
json_encorder_decorder.py

Created by Shota Shimazu on 2018/06/05

Copyright (c) 2018-2020 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import json
from typing import ClassVar


def encode(codable_instance: object) -> json:
    
    variables = codable_instance.__dict__.keys()
    values = codable_instance.__dict__.values()

    middle_dict = {}

    for i in range(len(variables)):
        middle_dict.setdefault(variables[i], values[i])

    return json.dumps(middle_dict)


def decode(data: json) -> (ClassVar, dict):
    pass
