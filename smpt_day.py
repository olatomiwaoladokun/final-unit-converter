# import smtplib
# smpt = smtplib.SMTP


import os, smtplib 

with open("page.py", "r") as file:
    data = file.read()

gmail_user = 'olatomiwaoladokun@gmail.com'
gmail_password = os.environ.get("GMAIL")

print(gmail_password)

sent_from = gmail_user

to = [
    # gmail_user,
    'dayopraisegod@gmail.com'
    ]
# 'adetoyeseoyekanmi@gmail.com',
# 'donaldogedengbe2@gmail.com',
# 'olatomiwaoladokun@gmail.com',
# 'olasund1@yahoo.com',
# 'oyekanmioreoluwa2007@gmail.com'

subject = "The requests module is not working"
body = data

email_text = """
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print("Email sent!")
except smtplib.SMTPAuthenticationError:
    print("Invalid credentials. Check your email and password...")
