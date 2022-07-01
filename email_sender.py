import smtplib, ssl


def send_email(recipient, email):    
    port = 465  
    smtp_server = "smtp.gmail.com"
    sender = "codefirstburner1@gmail.com"
    password = "wmhtzpiccjtomcgj"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email)
