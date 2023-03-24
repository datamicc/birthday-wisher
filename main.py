import datetime as dt
import smtplib
import random
#------------read the file ------------------------
with open('quotes.txt', 'r') as data:
    quotes = data.readlines()
    pick_quote = random.choice(quotes)
    # print(pick_quote)

#------------send email------------------------

my_email = 'data.micc@gmail.com'
my_password = 'tftlkineiozfxoka'

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='learn.micc@gmail.com',
            msg=f'Subject: Have a good day\n\n{pick_quote}'
        )



