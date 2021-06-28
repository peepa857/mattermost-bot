import json
import requests
from flask import Flask, request

BOT_TOKEN = 'BOT_TOKEN'
CHANNEL_ID = 'CHANNEL_ID'
MM_API_ADDRESS = 'http://xxx.xxx.xxx.xxx:8065/api/v4/posts'

app = Flask(__name__)


@app.route('/bot-test', methods=['POST'])  # 外向きのWebhookのコールバックURL
def bot_reply():
    posted_user = request.json['user_name']
    posted_msg = request.json['text']

    reply_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + BOT_TOKEN,
    }

    reply_data = {
        "channel_id": "CHANNEL_ID",
        "message": f"@{posted_user} Bot reply message.",
        "props": {
            "attachments": [{
                "author_name": posted_user,
                "text": posted_msg,
            }]
        },
    }

    reply_request = requests.post(MM_API_ADDRESS,
                                  headers=reply_headers,
                                  data=json.dumps(reply_data))

    return reply_request


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
