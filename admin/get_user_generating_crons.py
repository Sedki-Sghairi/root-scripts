#!/usr/bin/env python3
import re
import sys

logfile=sys.argv[1]
usernames={}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern,line)
        if result is None:
            continue
        print(result[1])