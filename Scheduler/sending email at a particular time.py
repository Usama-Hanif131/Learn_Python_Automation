"""program to send email on every friday at 12:19AM, email include attachement and that attachment is send
via encoded way of base64 encoding method
"""
import smtplib
import time
import schedule
from datetime import datetime 
import pytz
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase


def current_time():
    pak_timezone=pytz.timezone("Asia/Karachi")
    current_time=datetime.now(pak_timezone)
    formated_time=current_time.strftime("%I:%M:%S %p")
    return formated_time

def attach_body(your_msg,your_body):
    your_msg.attach(MIMEText(your_body,"plain"))
    return your_msg

def attach_file(attachment_path):
    with open(attachment_path, "rb") as file:
        part=MIMEBase("application","octet-stream")
        part.set_payload((file).read())
        file.close()
        return part

def encode_attachment(your_part):
    encoders.encode_base64(your_part)
    your_part.add_header("Content-Disposition", "attachment",filename='List.docx')
    return your_part

def make_smtp_connection(your_msg):
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=sender_email,password=token)
    connection.send_message(your_msg)
    connection.close()
    print("Mail has been send!")

def send_at_time(task):
    schedule.every().friday.at("00:19").do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
def send_email(From, To, Cc, subject, body, attachment):
    def myemail():
        msg=MIMEMultipart()
        msg["Subject"]=subject
        msg["From"]=From
        msg["To"]=To
        msg["Cc"]=Cc
        msg=attach_body(your_msg=msg,your_body=body)
        part=attach_file(attachment_path=attachment)
        part=encode_attachment(your_part=part)
        msg.attach(part)
        make_smtp_connection(your_msg=msg)
    send_at_time(myemail)

#program starting point
sender_email=""
reciever_email=""
manager_email=""
token=""
subject=f"Testing email from nginx server {current_time()}"
Body=f"""
Hi Team,
This is testing email form nginx server.
regards,
Admin
"""
path="E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Lecture#38 Email Module.docx"
send_email(From=sender_email,To=reciever_email,Cc=manager_email,subject=subject,body=Body,attachment=path)