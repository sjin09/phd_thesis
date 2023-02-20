#!/usr/bin/env python

import sys
from datetime import date

today = date.today()
d4 = today.strftime("%b-%d-%Y")
print(d4)
