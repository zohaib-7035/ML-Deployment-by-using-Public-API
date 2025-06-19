import json
import requests

url = 'https://39fb-103-131-213-142.ngrok-free.app//diabetes_prediction'  # ✅ URL is case sensitive

input_data = {
    "Pregnancies": 2,
    "Glucose": 85,
    "BloodPressure": 66,
    "SkinThickness": 29,
    "Insulin": 0,
    "BMI": 26.6,
    "DiabetesPedigreeFunction": 0.351,
    "Age": 31
}

response = requests.post(url, json=input_data)  # ✅ POST with json=

print(response.text)
