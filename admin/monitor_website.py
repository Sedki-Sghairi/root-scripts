import requests
import smtplib
import os
from linode_api4 import linodeClient, Instance

ACESS_TOKEN=os.environ.get('LINODE_TOKEN')
ID=os.environ.get('SERVER_INSTANCE_ID')
EMAIL=os.environ.get('MY_EMAIL')
EMAIL_RECIEVE=os.environ.get('MY_OTHER_EMAIL')
PASS=os.environ.get('MY_PASS')

r = requests.get('https://www.sedkisghairi.com', timeout=5)

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL,PASS)
        subject='Your Site is Down!'
        body='Site is Down, restart the server.'
        msg=f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL,EMAIL_RECIEVE,msg)
        
    client=linodeClient(ACESS_TOKEN)
    my_server = client.load(Instance, ID)
    my_server.reboot()

