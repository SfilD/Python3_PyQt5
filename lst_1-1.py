#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Проверка установки
import sys

print(tuple(sys.version_info))
try:
    raw_input()     # Python 2

except NameError:
    input()         # Python 3
