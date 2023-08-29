import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_otp(generated_otp, phone_number):
    url = "https://api.ng.termii.com/api/sms/otp/send"
    payload = {
            "api_key" : os.getenv('API_KEY'),
            "message_type" : "NUMERIC",
            "to" : phone_number,
            "from" : "N-Alert",
            "channel" : "dnd",
            "pin_attempts" : 10,
            "pin_time_to_live" :  5,
            "pin_length" : 6,
            "pin_placeholder" : "< 1234 >",
            "message_text" : generated_otp,
            "pin_type" : "NUMERIC"
        }
    headers = {
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.status_code)
