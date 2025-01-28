#!/usr/bin/env python3

import os
import datetime
import reports
import emails

report_path = "/tmp/processed.pdf"
title = f"Processed Update on {datetime.datetime.now().strftime('%Y-%m-%d')}"

# Generate the report data
report_data = []
for item in os.listdir('supplier-data/descriptions/'):
    with open('supplier-data/descriptions/' + item, 'r') as f:
        data = f.read().split('\n')
        name = data[0]
        weight = data[1]
        report_data.append(f"\n name: {name} \n weight: {weight} \n")
        
# Make usable with textLines
paragraph = "".join(report_data)

# info for email sending
from_email = "automation@example.com"
to_email = "student@example.com"
subject_line = "Upload Completed - Online Fruit Store"
email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

if __name__ == "__main__":
      reports.generate_report(report_path, title, paragraph)
      message = emails.generate_email(from_email, to_email, subject_line, email_body, report_path)
      emails.send_email(message)


