import smtplib
import ssl


def send_recovery_code(recovery_message):
    port = 2828
    smtp_server = ""
    sender_email = "place_holderemail@email.com" #placeholder email until smtp server is configured
    password = "Password" #placeholder until smtp server is configured

    receiver_email = recovery_message.user_email
    recovery_code = recovery_message.code

    message = """
    Subject: Smart Caring Password Recovery Code
    
    
    Your Smart Caring password recovery code is: $recovery_code
    This code will expire in 5 minutes.

    If you did not request a password change, you can safely ignore this e-mail.
    """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)