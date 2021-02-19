#!/usr/bin/env python3

import os, datetime
import reports
import emails


current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generatedf(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if file.endswith(".txt"):
      with open(path + file, 'r') as f:
        inline = f.readlines()
        name = inline[0].strip()
        weight = inline[1].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  path = "supplier-data/descriptions/"
  title = "Process Updated on " + current_date 
  package = generate_pdf(path)
  reports.generate_report("/tmp/processed.pdf", title, package)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  
  #send email with pdf attachment
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)


  



