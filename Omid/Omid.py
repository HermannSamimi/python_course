import requests
import json
import os
import dotenv
# Load environment variables from .env file
dotenv.load_dotenv()
from time import sleep


# ------------------------------------------ get data from an API ----------------
# RAPID API LINK : https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates/playground/endpoint_01c2f371-2ab0-4e56-98f4-e4f4149e9cfc
url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/timeseries"

start_date = "2025-06-01" #June = 6
end_date = "2025-06-20"
base_currency = "USD"
symbols = "THB, DKK"

querystring = {
    "start_date": start_date,
    "end_date": end_date,
    "base": base_currency,
    "symbols": symbols
}

headers = {
	"x-rapidapi-key": "11c830c25emshf8289b2a0f0cecep1a192fjsna96600ee8ec1",
 	"x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
 }

response = requests.get(url, headers=headers, params=querystring)

output = response.json()
print(json.dumps(output, indent=4))

# =========================== # save data to a file ------------------------
raw_file = r"D:\My Documents\My Downloads\Learning\Python\python_course-1\Omid\Raw_rate.json"
thb_path = r"D:\My Documents\My Downloads\Learning\Python\python_course-1\Omid\THB.json"
dkk_path = r"D:\My Documents\My Downloads\Learning\Python\python_course-1\Omid\DKK.json"
with open(raw_file, "w") as file:
     json.dump(output, file, indent=4)



# i want to read the raw file
with open(raw_file, 'r') as read_file:
    read_raw_file = json.load(read_file)
    b_data = json.dumps(read_raw_file, indent=4)
    print(b_data)
    print(type(read_raw_file))


    
thb_data = {}
dkk_data = {}

# filter THB ==========================================
for date, rates in read_raw_file["rates"].items():
    thb_rate = rates.get("THB", "N/A")
    thb_data[date] = thb_rate

with open(thb_path, 'w') as thb_file:
    json.dump(thb_data, thb_file, indent=4)




# filter DKK ==========================================
for date, rates in read_raw_file["rates"].items():
    dkk_rate = rates.get("DKK", "N/A")
    dkk_data[date] = dkk_rate


with open(dkk_path, 'w') as eur_file:
    json.dump(dkk_data, eur_file, indent=4)

# ------------------------ # create a telegram bot -------------------------

# for i in range (10):
#     BOT_TOKEN = os.getenv("telegram_token")
#     CHAT_ID = "-1002830405443"

#     MESSAGE = f"{i}"


#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

#     payload = {
#         "chat_id": CHAT_ID,
#         "text": MESSAGE
#     }

#     response = requests.post(url, data=payload)

#     if response.status_code == 200:
#         print("Message sent successfully.")
#     else:
#         print("Failed to send message:", response.text)
#     sleep(3)  


# # slack message :
# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

# message = "Hello, Slack!"

# def send_message(text: str):
#     payload = {
#         "text": text
#     }
#     resp = requests.post(SLACK_WEBHOOK, json=payload)
#     resp.raise_for_status()

# os.environ["SLACK_WEBHOOK"] = "https://hooks.slack.com/services/…"
# send_message(message)