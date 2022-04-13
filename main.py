import pandas
import datetime
import smtplib
import random

"""
Problem with this file is: To check everyday the script muss run in the background 
running the program everyday is too much effort 

So we can could use a service called Python anywhere, free trial where we can host our code without paying 
"""

# read content
# optional :  no index of column please - so that we get the right values for the attribute  index_col=0
df = pandas.read_csv("birthdays.csv")

# get date
# create a tuple with the necessary values we need to compare
# accessing [month] from the now method of the datetime class of the datetime module
today = (datetime.datetime.now().month, datetime.datetime.now().day)

# -------------------------------- SMTP INFORMATION'S  -------------------------------- #
MY_EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
# ------------------------------------------------------------------------- #

# in the most cases without index configuration on top we have a number
for (index, person) in df.iterrows():
    # if person has today birthday
    if today == (person["month"], person["day"]):
        # 1 and 3 included
        file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        # reading and preparing letter
        with open(file_path, "r") as letter:
            letter_content = letter.readlines()
            new_header = letter_content[0].replace("[NAME]", person["name"])
            new_footer = letter_content[-1].replace("Angela", "Markus")
            letter_content = new_header + \
                "".join(letter_content[1:-1]) + "".join(new_footer)
        # build now smtp connection and sent the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person.email,
                msg=f"Subject:Happy Birthday\n\n{letter_content}"
            )
