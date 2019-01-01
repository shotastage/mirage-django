"""
MIRAGE Framework
types.py

Created by Shota Shimazu on 2018/06/05

Copyright (c) 2018-2019 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

from typing import NoReturn
from django.http import HttpRequest, HttpResponse

# Basic Types
Void = NoReturn
String = str
Int = int
Float = float

# Django Types
Request = HttpRequest
Response = HttpResponse
