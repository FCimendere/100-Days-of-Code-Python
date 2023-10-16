#Project : ISS Overhead Notifier
"""
PRACTISE: SMTP library usage, API endpoint practise
PROJECT: An email will be sent during the nighttime if the ISS satellite is overhead user location.
In this project, API endpoint,smtplib, datetime lib has been used. 
"""

import requests
from datetime import datetime
import smtplib
import math
import time

# Your latitude
MY_LAT = 52.291611
# your longitude
MY_LONG = 4.578690
REQUEST_PERIOD = 60


def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    # get sunrise and sunset time of your location
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = response.json()["results"]['sunrise'].split("T")[1].split(":")[0]
    sunset = response.json()["results"]['sunset'].split("T")[1].split(":")[0]
    # get the present time of user
    time_now = datetime.now()
    # print(time_now.hour)
    if time_now.hour not in range(int(sunrise), int(sunset)):
        return True


def is_iss_overhead():
    # get the ISS current position
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    iss_lat = float(response_iss.json()['iss_position']['latitude'])
    iss_long = float(response_iss.json()['iss_position']['longitude'])
    if (math.isclose(MY_LAT, iss_lat, abs_tol=0.4)) and (math.isclose(MY_LONG, iss_long, abs_tol=0.4)):
        return True


# smtp settings
my_email = "home@gmail.com"
password = "vxalzztlihmbobto"

while True:
    time.sleep(REQUEST_PERIOD)
    if is_iss_overhead() and is_night():
        print("log")
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="test@gmail.com",
                                msg="Subject:ISS Satellite information n\n"
                                    "Hey,There is an ISS Satellite above your location."
                                    "\n Look at the sky!")