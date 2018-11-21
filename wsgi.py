# http://url.com?type=Diesel

import os
from telethon import TelegramClient, sync
from telethon.sessions import StringSession
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
	#for message in client.get_message_history('@' + botname, limit=10):
    #print(utils.get_display_name(message.sender), message.message)
    client.disconnect()
    return "Hello!"

if __name__ == "__main__":
  application.run()
