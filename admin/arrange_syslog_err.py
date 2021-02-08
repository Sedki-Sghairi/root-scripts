#!/usr/bin/env python3
import sys
import os
import re
import csv

per_user_errors ={}

with open("syslog.log") as f:
    for log in f:
      pattern=r" \((\w+)\)$"
      result = re.search(pattern,log)
      user=result[1]
      if "ERROR" in log:
          if user not in per_user_errors:
              per_user_errors[user]={"ERRORS":0,"INFO":0}
          per_user_errors[user]["ERRORS"]+=1
      elif "INFO" in log:
          if user not in per_user_errors:
              per_user_errors[user]={"ERRORS":0,"INFO":0}
          per_user_errors[user]["INFO"]+=1    
          
    print(per_user_errors)
