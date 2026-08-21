# ISS Overhead Notifier

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.394287 # Your Latitude
MY_LONG = 77.112602 # Your Longitude

my_email = "youremail@gmail.com"
password = "your_password"

def near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Mention if any error takes place
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)

def is_dark():
    parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Split to get the hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return sunset < time_now < sunrise

while True:
    # Send email if iss is near and it is dark
    if near_me() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject: ISS\n\nLook Up!"
                                )
    # Test for every 60s
    time.sleep(60)




