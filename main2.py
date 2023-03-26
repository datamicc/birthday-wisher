##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.date()
year = today.year
month = today.month
day = today.day


birthdays = pandas.read_csv('birthdays.csv')
birthdays_list = birthdays.to_dict(orient="records")
# print(birthdays_list)

new_dict = next(item for item in birthdays_list if item['year'] == year and item['month'] == month and item['day'] == day)
friend_name = new_dict['name']
friend_email = new_dict['email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

letter_number = str(random.randint(1,3))

with open(f'letter_templates/letter_{letter_number}.txt') as letter:
    letter_content = letter.read()
    letter_content = letter_content.replace('[NAME]', friend_name)
    # print(letter_content)

# 4. Send the letter generated in step 3 to that person's email address.
my_email = 'data.micc@gmail.com'
my_password = 'tftlkineiozfxoka'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=friend_email,
        msg=f'Subject: Happy Birthday!\n\n{letter_content}'
    )