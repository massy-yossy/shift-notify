import requests
import os
import json

CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_TOKEN")
USER_ID = os.getenv("LINE_USER_ID")

def send_line(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    res = requests.post(url, headers=headers, data=json.dumps(payload))
    print(res.status_code, res.text)

if __name__ == "__main__":
    send_line("✅ STEP1成功！Messaging API からのテスト通知です")
