import smtplib
import ssl


def send_recovery_code(recovery_message):
    port = 2828
    smtp_server = ""
    sender_email = "no-reply@smartcaring.com"
    password = input("Password")

    receiver_email = recovery_message.email
    recovery_code = recovery_message.code

    message = """
    Subject: Smart Caring Password Recovery Code
    
    Your Smart Caring password recovery code is: $recovery_code
    If you did not request a password change please ignore this e-mail.
    """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
