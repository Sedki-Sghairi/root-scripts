#!/usr/bin/env python3

import psutil, shutil
import socket
import emails
import os 
import sys

def cpu_check():
  cpu_usage = psutil.cpu_percent(1) 
  return cpu_usage > 80

def disc_space_check():  
  disk_usage = shutil.disk_usage("/")
  disk_free = disk_usage.free/disk_usage.total*100
  return disk_free < 20

def available_memory_check():
  x = psutil.virtual_memory().available
  available = x / 1024 ** 2 
  return available < 500

def hostname_check():
  ip = socket.gethostbyname('localhost')
  return ip != "127.0.0.1"

def email_warning(error):
  user = os.environ["USER"]
  sender = "automation@example.com"
  receiver = "{}@example.com".format(user)
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.send_email(message)

if cpu_check():
  subject = "Error - CPU usage is over 80%"
  email_warning(subject)

if disc_space_check():
  subject = "Error - Available disk space is less than 20%"
  email_warning(subject)

if available_memory_check():
  subject = "Error - Available memory is less than 500MB"
  email_warning(subject)

if hostname_check():
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  email_warning(subject)
