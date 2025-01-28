#!/usr/bin/env python3

import requests
import os

upload_location = "http://<IP>/upload/"

for file in os.listdir('supplier-data/images/'):
    if file.endswith('.jpeg'):
        with open('supplier-data/images/' + file, 'rb') as opened:
            r = requests.post(upload_location, files={'file': opened})
            if r.status_code != 201:
                raise Exception("POST failed! | Status code: {} | File: {}".format(r.status_code, file))
            else:
                print("Success! | Status code: {} | File: {}".format(r.status_code, file))
                