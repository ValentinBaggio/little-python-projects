import smtplib

sender = "valenbaggio@outlook.com"

receiver = "vickybaggio50@gmail.com"

password = "Mifacebook1$"

subject = "Python email test :)"

body = "Escribi esto con la compu xdddddd, contestame si lo viste"

#header

message = f"""From Snoop Dog{sender}
{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.outlook.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("log in")
    server.sendmail(sender, receiver, message)
    print("email has been sent")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")