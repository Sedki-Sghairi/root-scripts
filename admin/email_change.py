#!usr/bin/env python3
import re
import csv

def contains_domain(address,domain):
    domain = r'[\w\.-]+@' + domain + '$'
    if re.match(domain,address):
        return True
    return False    

def replace_domain(address,old_domain,new_domain):
    """replace old domain with the new one in given-address"""
    old_domain_pattern=r'' + old_domain + '$'
    address = re.sub(old_domain_pattern,new_domain,address)
    return address