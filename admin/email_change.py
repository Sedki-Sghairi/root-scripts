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

def main():
    """process list of emails, replacing old domain-names"""
    old_domain, new_domain = 'example.edu','abc.edu'
    csv_file="/home/kali/my_file"
    report_file='/home' + '/updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list=[]    
    new_domain_email_list=[]

    with open(csv_file, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

        