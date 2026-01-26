import requests
import os
import json

CHANNEL_ACCESS_TOKEN = os.getenv("UHEBH46clWWCzcKGu/NMHuqEOktnxzHdG/ABvj7xZYgUm5Oe/2kTKVhVuvy82P7eE97owV3mLhaFBw5vqp0BYCRkffDVaU/pLu/zENvXiDMhfMWPPD0KAMeWtIjfJeIZ09aK28G/Uy30cAn9suzvFQdB04t89/1O/w1cDnyilFU=")
USER_ID = os.getenv("Ubaa71a296fd5f09b4488822497a3d1fb")

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
