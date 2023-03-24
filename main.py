import smtplib

my_email = 'data.micc@gmail.com'
my_password = 'tftlkineiozfxoka'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs='learn.micc@gmail.com', msg='Subject: Happy Birthday\n\nHello')
connection.close()