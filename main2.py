##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.date()
year = today.year
month = today.month
day = today.day


birthdays = pandas.read_csv('birthdays.csv')
birthdays_dict = birthdays.to_dict(orient="records")
print(birthdays_dict)

for i in birthdays_dict:
    if birthdays_dict[i]['year'] == year and birthdays_dict[i]['month'] == month and birthdays_dict[i]['day'] == day:
        friend_name = birthdays_dict[i]['name']
        friend_email = birthdays_dict[i]['email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.