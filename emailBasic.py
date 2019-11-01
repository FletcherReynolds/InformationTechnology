import smtplib

email = "goodsphepherdiot@gmail.com"  # your email
password = 'p@ssword#1'  # your email account password
send_to_email = 'fletcherreynolds@outlook.com'  # recipient
message = 'yes this in the message'  # message in body of email

server = smtplib.SMTP('smtp.gmail.com', 587)  # connect to the server
server.starttls()  # use TLS (transport layer security)
server.login(email, password)
server.sendmail(email, send_to_email, message)
server.quit()