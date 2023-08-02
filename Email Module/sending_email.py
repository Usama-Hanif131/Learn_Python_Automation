import smtplib
sender_email = "" 
target_email = ""
token = "" #enter sender gmail smtp server secret password
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=sender_email, password=token)
connection.sendmail(from_addr=sender_email, to_addrs=target_email, msg="This is a test email")
connection.close()
print("Email send successfully")