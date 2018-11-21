# http://url.com?type=Diesel

import os
import time
from telethon import TelegramClient, sync
from telethon import utils
from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def hello():
    api_id = os.environ['apiidWebHookSecretKey']
    api_hash = os.environ['apihashWebHookSecretKey']
    botname = os.environ['botnameWebHookSecretKey']
    typ = request.args.get('type')
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    client.send_message('@' + botname, typ)
    time.sleep( 5 )
    for message in client.iter_messages('@' + botname, limit=1):
      print(message.message)

    client.disconnect()
    return "Hello!"

if __name__ == "__main__":
  application.run()
