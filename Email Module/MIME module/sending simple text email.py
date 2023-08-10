import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email=""
reciever_email=""
manager_email=""
token=""
subject="Testing email from Nagios!"
body="\bHi\bteam,\nThis is testing email from Nagios server!"
msg=MIMEMultipart()
msg["Subject"]=subject
msg["From"]=sender_email
msg["To"]=reciever_email
msg["Cc"]=manager_email
msg_ready=MIMEText(body,"plain")
msg.attach(msg_ready)

connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=sender_email,password=token)
connection.send_message(msg)
connection.close()
print("Mail has been send!")

