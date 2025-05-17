import requests
from django.conf import settings

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message(fullname, phone, region):
    text = f"Yangi mijoz!\n\nIsm: {fullname}\nTelefon: {phone}\nHudud: {region}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)
