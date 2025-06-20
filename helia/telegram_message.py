import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your values
BOT_TOKEN = os.getenv("telegram_token")
CHAT_ID = "-1002830405443"
MESSAGE = "helia"

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

