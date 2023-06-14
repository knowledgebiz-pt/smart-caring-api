import smtplib
import ssl


def send_recovery_code(response_database, code):
    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "dev@knowledgebiz.pt"
    password = "Vuw20954"

    receiver_email = response_database["email"]
    recovery_code = code

    message = """
    Your Smart Caring password recovery code is: %r
    This code will expire in 5 minutes.

    If you did not request a password change, you can safely ignore this e-mail.
    """ % recovery_code

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
