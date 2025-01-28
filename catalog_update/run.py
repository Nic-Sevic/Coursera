#! /usr/bin/env python3

import os
import requests

for item in os.listdir('supplier-data/descriptions/'):
# convert txt to JSON dictionary
# include associated image with .jpeg extension
# upload to http://[external-IP-address]/fruits
  with open('supplier-data/descriptions/' + item, 'r') as f:
    data = f.read().split('\n')
    fruit = {
      "name": data[0],
      "weight": int(data[1].split()[0]),
      "description": data[2],
      "image_name": item.split('.')[0] + '.jpeg'
    }
    response = requests.post('http://<IP>/fruits/', json=fruit)

