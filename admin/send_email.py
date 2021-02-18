
import os
import smtplib
import mimetypes
#import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Meet for coffee and code.'
msg['From'] = os.environ.get('SENDER')
msg['To'] = os.environ.get('RECEIVER')
msg.set_content('How about 10, this saturday?')

attachement_path = '/opt/icons/toothless.png'
mime_type , _ =mimetypes.guess_type(attachement_path)
mime_type, mime_subtype = mime_type.split('/',1)
with open(attachement_path, 'rb') as f:
    file = f.read()
    msg.add_attachment(file,
    maintype=mime_type,
    subtype=mime_subtype,
    filename=os.path.basename(attachement_path))

#mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
#mail_server.set_debuglevel(1)
#mail_server.login(os.environ.get('SENDER'),os.environ.get('PASS'))
#mail_server.send_message(msg)
#mail_server.quit()
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(os.environ.get('SENDER'),os.environ.get('PASS'))
    smtp.send_message(msg)