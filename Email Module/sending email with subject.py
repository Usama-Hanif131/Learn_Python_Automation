import smtplib
sender_email=""
token="" #enter sender gmail smtp server secret password
receiver_email=""
Subject="High usage of RAM"
body="Hi team,\nwe are notice some high usage of RAM in production Server above 90%. kindly login and check the background processes.\nRegards,"
message=f"From: {sender_email}\nTo: {receiver_email}\nSubject: {Subject}\n\n{body}"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=sender_email,password=token)
connection.sendmail(from_addr=sender_email,to_addrs=receiver_email,msg=message)
connection.close()
print("email send successfully")