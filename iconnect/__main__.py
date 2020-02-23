#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 baneon - MIT License
# See `LICENSE.md` included in the source distribution for details.

__version__ = "1.0"

"""internet connection.

Check your internet connection

"""


import sys
import requests

from requests.exceptions import Timeout, ConnectionError
from contextlib import closing


SUCCESS = 0
NOT_FOUND = 1

OK = requests.codes['OK']

attempts = 3
url = 'http://172.217.15.206/' # https://www.google.com/


def main(args):
    for i in range(0, attempts):
        try:
            with closing(requests.get(url, timeout=10)) as r:
                if r.status_code == OK:
                    return SUCCESS
        except Timeout:
            print('attempts: {}'.format(i+1))
        except ConnectionError:
            print('No network connection detected')
            break

    return NOT_FOUND
