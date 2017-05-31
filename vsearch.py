# -*- coding: utf-8 -*-

import csv
import requests
with open ('routine.csv',encoding='utf8')as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
       