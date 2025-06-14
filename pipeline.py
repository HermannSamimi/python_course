import requests
import json
import os
import dotenv
# Load environment variables from .env file
dotenv.load_dotenv()
from time import sleep


# ------------------------ # Example of using an API to get movie data ------------------------


# url = "https://movie-database-api1.p.rapidapi.com/list_movies.json"

# querystring = {"limit":"20","page":"1","quality":"all","genre":"all","minimum_rating":"0","query_term":"0","sort_by":"date_added","order_by":"desc","with_rt_ratings":"false"}

# headers = {
#     "x-rapidapi-key": "11c830c25emshf8289b2a0f0cecep1a192fjsna96600ee8ec1",
#     "x-rapidapi-host": "movie-database-api1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# data = response.json()
# data = json.dumps(data, indent=4)

# print(data)



# ------------------------ # Example of read data from a txt file  ------------------------
# read data from a file
with open("/Users/hermann/Documents/Python Course/data/test_persian.txt", "r") as file:
    data = file.read()



# ------------------------ # create a telegram bot -------------------------

# Replace with your values
    BOT_TOKEN = os.getenv("telegram_token")
    CHAT_ID = "-1002830405443"

    MESSAGE = data


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
    sleep(1)  



