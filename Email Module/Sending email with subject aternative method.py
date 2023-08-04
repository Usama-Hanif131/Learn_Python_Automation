from email.message import EmailMessage
import smtplib
sender_email="muhammadosama0121@gmail.com"
reciever_email="i9460131@gmail.com"
manager_email="usa353642@gmail.com"
token="pvvdjfuksgosoysh"
#setting up email structure 
msg=EmailMessage()
msg["Subject"]="Alert from Nagios server!"
msg["From"]=sender_email
msg["To"]=reciever_email
msg["Cc"]=manager_email
msg.set_content("Hi Team,This is testing email from nagios server!") #email body 
#code for attachment
with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\file1.txt","rb") as f:
    attachment=f.read()
    file_name=f.name
f.close()
msg.add_attachment(attachment,maintype="application",subtype='octect-stream',filename=file_name)
#making connection with smtp server
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
#login with credentials and sending email
connection.login(user=sender_email, password=token)
connection.send_message(msg)
connection.close()
print("Message has been sent successfully")