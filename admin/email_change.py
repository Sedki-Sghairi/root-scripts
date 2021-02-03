#!usr/bin/env python3
import re
import csv

def contains_domain(address,domain):
    domain = r'[\w\.-]+@' + domain + '$'
    if re.match(domain,address):
        return True
    return False    