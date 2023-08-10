import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#ready email
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
msg.attach(MIMEText(body,"plain"))

#attach attachment 
path="E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Lect#10 List.docx" 
with open(path, "rb") as attachment:
    part=MIMEBase("application","octet-stream")
    part.set_payload((attachment).read())
attachment.close()
#encode the attachment
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment",filename='List.docx')
msg.attach(part)

#sending email
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=sender_email,password=token)
connection.send_message(msg)
connection.close()
print("Mail has been send!")