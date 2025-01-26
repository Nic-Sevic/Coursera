#!/usr/bin/env python3

# This script will process a directory of text files and upload the content to a web service.
# Data format: [{"id":1,"title":"Experienced salespeople","name":"Alex H.","date":"2020-02-02","feedback":"It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}]

import os
import requests

def post_feedback(feedback):
	url = "http://35.233.140.102/feedback/"
	response = requests.post(url, json=feedback)
	if response.status_code == 201:
		print("Feedback uploaded successfully")
	else:
		print(f"Error uploading feedback: {response.status_code}")

feedback_Files = os.listdir("/data/feedback/")

for file in feedback_Files:
        with open(f"/data/feedback/{file}", "r") as f:
                lines = f.readlines()
                post_feedback({
                        "title": lines[0].strip(),
                        "name": lines[1].strip(),
                        "date": lines[2].strip(),
                        "feedback": lines[3].strip()
                })
