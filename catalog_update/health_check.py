#!/usr/bin/env python3

# Description: Will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems

import shutil
import psutil
import socket
import emails
import time

# Check if CPU usage is over 80%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    if usage > 80:
      return "Error - CPU usage is over 80%"

# Check if available disk space is lower than 20%
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    if free < 20:
      return "Error - Available disk space is less than 20%"

# Check if available memory is less than 100MB
def check_memory_usage():
    usage = psutil.virtual_memory()
    if usage.available < 100 * 1024 * 1024:
      return "Error - Available memory is less than 100MB"

# Check if the hostname "localhost" cannot be resolved to "127.0.0.1"
def check_localhost():
    if socket.gethostbyname('localhost') != '127.0.0.1':
      return "Error - localhost cannot be resolved to 127.0.0.1"

# Send an email if there are problems
def send_email(subject_line):
  from_email = "automation@example.com"
  to_email = "student@example.com"
  email_body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(from_email, to_email, subject_line, email_body)
  emails.send_email(message)

# Perform checks
if __name__ == "__main__":
  checks = [check_cpu_usage(), check_disk_usage("/"), check_memory_usage(), check_localhost()]
  for check in checks:
    if check:
      send_email(check)

# can set cron job with 'crontab -e' to run every 60 seconds in background
