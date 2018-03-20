import os
from telethon import TelegramClient
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    api_id = os.environ['apiidWebHookSecretKey']
    api_hash = os.environ['apihashWebHookSecretKey']

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    #print(client.get_me().stringify())
    client.send_message('@' + os.environ['botnameWebHookSecretKey'], 'Diesel')

    return "Hello World!"
    
if __name__ == "__main__":
  application.run()
