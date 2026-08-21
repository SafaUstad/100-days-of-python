# Birthday Wisher
import smtplib
import datetime as dt
import pandas
import random

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

for index, row in data.iterrows():
    if row["month"] == today.month and row["day"] == today.day:
        random_letter = random.randint(1,3)
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random_letter}.txt", "r") as f:
            letter = f.read().replace("[NAME]", row["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = "youremail@gmail.com"
        password = "your_password"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject: Birthday Wish!\n\n{letter}"
                                )









