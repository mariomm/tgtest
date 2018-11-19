# http://url.com?type=Diesel

import os
from telethon import TelegramClient, sync
from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def hello():
    api_id = os.environ['apiidWebHookSecretKey']
    api_hash = os.environ['apihashWebHookSecretKey']
    botname = os.environ['botnameWebHookSecretKey']
    typ = request.args.get('type')
    #parama = request.args.get('parama')
    #paramb = request.args.get('paramb')
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()   
    client.send_message('@' + botname, typ)

    return "Hello!"
    
if __name__ == "__main__":
  application.run()
