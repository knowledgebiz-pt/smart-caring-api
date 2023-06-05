import smtplib
import ssl


port = 2828
smtp_server = ""
sender_email = "no-reply@smartcaring.com"
password = input("Password")

receiver_email = ""

message = """
Subject: Smart Caring Password Recovery Code

Your Smart Caring password recovery code is:
If you did not request a password change please ignore this e-mail.
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
