#!/usr/bin/env python3
import sys
import os
import re
import csv
import operator
per_user_errors = {}
per_error = {}
with open("syslog.log") as f:
    for log in f:
      pattern=r" \((\w+)\)$"
      result = re.search(pattern,log)
      user=result[1]
      if "ERROR" in log:
          if user not in per_user_errors:
              per_user_errors[user]={"ERRORS":0,"INFO":0}
          per_user_errors[user]["ERRORS"]+=1
          error_pattern=r"[EROR]{5} .* \("
          res=re.search(error_pattern,log)
          error=res.group()[6:-2]
          if error not in per_error:
              per_error[error] = 0
          per_error[error] += 1
      elif "INFO" in log:
          if user not in per_user_errors:
              per_user_errors[user]={"ERRORS":0,"INFO":0}
          per_user_errors[user]["INFO"]+=1
          
a=dict(sorted(per_user_errors.items(), key=lambda item:item[0]))          
b=dict(sorted(per_error.items(), key=lambda item:item[1], reverse=True))          

with open("per_user_report.csv","w") as file:
    please = csv.writer(file)
    please.writerow(['Username', 'INFO', 'ERROR'])
    for i in a:
        please.writerow([i, a[i]["ERRORS"], a[i]["INFO"]])

with open("per_error_report.csv","w") as csvf:
    please = csv.writer(csvf)
    please.writerow(["Error_message", "Count"])
    for m in b:
        please.writerow([m, b[m]])

