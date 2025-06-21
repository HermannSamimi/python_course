import requests
import json
import os
import dotenv
# Load environment variables from .env file
dotenv.load_dotenv()
from time import sleep


# ------------------------------------------ get data from an API ----------------
# RAPID API LINK : https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates/playground/endpoint_01c2f371-2ab0-4e56-98f4-e4f4149e9cfc
import requests


# start_date = 
# end_date = 
# base = "USD"
# symbols = "EUR,GBP"

# url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/timeseries"

# querystring = {"start_date":"2025-01-01","end_date":"2019-01-30","base":"USD","symbols":"EUR,GBP"}

# headers = {
# 	"x-rapidapi-key": "11c830c25emshf8289b2a0f0cecep1a192fjsna96600ee8ec1",
# 	"x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# output = response.json()
# print(json.dumps(output, indent=4))



# # ------------------------ # Example of read data from a txt file  ------------------------
# # read data from a file
# with open("/Users/hermann/Documents/Python Course/data/test_persian.txt", "r") as file:
#     data = file.read()



# ------------------------ # create a telegram bot -------------------------

while True:
    BOT_TOKEN = os.getenv("telegram_token")
    CHAT_ID = "-1002830405443"

    MESSAGE = "data"


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

