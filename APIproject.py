import requests
import datetime


APP_ID = "fd75fce8"
APP_KEY = "5836ae04e03536c44ef7d765545b03b9"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("Tell me which exercises you did: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": text,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 180,
    "age": 23
}

response = requests.post(endpoint, json=parameters, headers=header)
result = response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/faa23ae0b76105bf02879ba6c3fd89d7/workoutTracking/workouts"

sheety_headers = {
    "Authorization": "Basic YXZhbnRicmF0Y2g6c2h1Ym5pZ2d1cmF0aA==",
}

current_time = datetime.datetime.now()
time = current_time.strftime("%H:%M:%S")
print(time)

date = current_time.strftime("%d/%m/%Y")
time = current_time.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    input_info = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheety_endpoint, json=input_info, headers=sheety_headers)
print(sheet_response.text)
