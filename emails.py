import os
import smtplib
from email.message import EmailMessage
import mimetypes

with open('IMPORTANT!!!.txt') as file:
    email_input = file.read().split('\n')[1:3]
    # you can change this variable value by your environtment variable
    # but keep in mind you have to activate less secure in your google setting first
    # or make some app password for EMAIL_PASS variable in google setting
# EMAIL_USER = os.environ.get('EMAIL_USER')
# EMAIL_PASS = os.environ.get('PYTHON_EMAIL')
EMAIL_USER, EMAIL_PASS = email_input


def generate_email(reciever, subject, content, attechment_list=[]):
    msg = EmailMessage()
    msg['From'] = EMAIL_USER
    msg['To'] = reciever
    msg['Subject'] = subject
    msg.set_content(content)

    for i in attechment_list:
        with open(i, 'rb') as file:
            file_data = file.read()
            mime_type = mimetypes.guess_type(i)[0]
            mime_type, mime_subtype = mime_type.split('/')

        msg.add_attachment(file_data, maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(i))

    return msg


def send_email(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)