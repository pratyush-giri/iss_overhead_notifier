import time

import requests
from datetime import datetime
import smtplib
MY_EMAIL = "pratyushgiri133@gmail.com"
MY_PWD = "@pratyush123"
MY_LAT = 22.260424
MY_LONG = 84.853584



def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT-5 <=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True



def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(":")[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now > sunset and time_now < sunrise:
        return True



while True:
    time.sleep(120)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PWD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up\n\n the ISS is above you"
        )




