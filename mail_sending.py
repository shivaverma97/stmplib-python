import smtplib
import imghdr
import os
from email.message import EmailMessage

email_address = os.environ.get('server_mail')           # environment variables
email_pass = os.environ.get('server_pass')

contacts = ['add the list of senders email here']         # for multiple receivers

msg = EmailMessage()
msg['Subject'] = 'Testing attachments'
msg['From'] = email_address
msg['To'] = contacts                 # for mutiple receivers, if not then just type main receiver email here only
msg.set_content = 'This is a script.'

img_files = ['test.png','test_2.png','sample.pdf']                   # for multiple images use loop as written below to attach multiple images 

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1>Hello, trying something new!!</h1>
    </body>
</html>
""", subtype='html')                                         # for attractive looks, we have added html here

for img_file in img_files:
    with open(f'c:\\Users\\shiva\\OneDrive\\Desktop\\prac\\01 corey schafer\\sending_emails_smtplib\\{img_file}', 'rb') as img :
        img_data = img.read()
        img_type = imghdr.what(img.name)
        img_name = img.name
    _, img_file_ext = os.path.splitext(img_file)
    if img_file_ext == '.png' or img_file_ext == '.jpeg' :
        msg.add_attachment(img_data, maintype='image', subtype=img_type, filename=img_name)
    if img_file_ext == '.pdf' :                                   # for bit type attachments
        msg.add_attachment(img_data, maintype='application', subtype='octet-stream', filename=img_name)

# for testing use this in cmd for debug server 
# python -m smtpd -c DebuggingServer -n localhost:1025
# with smtplib.SMTP('localhost',1025) as smtp :                   # for local server

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp :            # TLS for live server
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp :        #SSL
#     # smtp.ehlo()           #ONLY FOR TLS   identify ourselve as a connection to the mail server we are using, NOT REQUIRED TO WRITE MANUALLY. It is called automatically.
#     # smtp.starttls()       #ONLY FOR TLS   this is to encrypt the traffic
#     # smtp.ehlo()           #ONLY FOR TLS   re-identifying ourselves as a encrypted connection, AGAIN NOT REQUIRED< IT IS DONE AUTOMATICALLY
    smtp.login(email_address,email_pass)
    smtp.send_message(msg)
    
 



