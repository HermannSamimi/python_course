import json
import os
from dotenv import load_dotenv
import requests
from time import sleep
load_dotenv()
# ------------------------------------------

eur = "/Users/hermann/Documents/Python Course/python_course/data/eur.json"

with open(eur, 'r') as file:
    data = json.load(file)


    for date, rate in data.items():
        print(f"Date: {date}, Rate: {rate}")
        if rate >= 0.89:
            BOT_TOKEN = os.getenv("telegram_token")
            CHAT_ID = "-1002830405443"
            MESSAGE = f"Date: {date}, Rate: {rate}"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

            payload = {
                "chat_id": CHAT_ID,
                "text": MESSAGE
            }

            response = requests.post(url, data=payload)

            if response.status_code == 200:
                print("Message sent successfully.")
            else:
                print("Failed to send message:", response.text)
            sleep(3)

