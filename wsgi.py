import os
from telethon import TelegramClient
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    api_id = os.environ['apiidWebHookSecretKey']
    api_hash = os.environ['apihashWebHookSecretKey']
    botname = os.environ['botnameWebHookSecretKey']
   
    
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()   
    client.send_message('@' + botname, 'Diesel')

    return "Hello!"
    
if __name__ == "__main__":
  application.run()
