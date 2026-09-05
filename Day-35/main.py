import requests
from twilio.rest import Client

account_sid = "your_acc_sid"
auth_token = "your_auth_token"
API_KEY = "your_api_key" 
MY_LAT = 14.5995 # Your Latitude
MY_LONG = 120.9842 # Your Longitude
weather_list = []

parameters = {
    "appid": API_KEY,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4
}

response = requests.get(url= f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for n in range(4):
    weather_id = data["list"][n]["weather"][0]["id"]
    weather_list.append(weather_id)
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's gonna rain. Remember to bring an ☂️.",
        from_="+17372212163",
        to="test_phone_number",
    )
    print(message.status)
