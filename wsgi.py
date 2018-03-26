import os
from telethon import TelegramClient
from flask import Flask
from cgi import parse_qs
application = Flask(__name__)

@application.route("/")
def hello(environ, start_response):
    api_id = os.environ['apiidWebHookSecretKey']
    api_hash = os.environ['apihashWebHookSecretKey']
    botname = os.environ['botnameWebHookSecretKey']
    d = parse_qs(environ['QUERY_STRING'])
    age = d.get('age', [''])[0]
    
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()   
    client.send_message('@' + botname, age)

    return "Hello!"
    
if __name__ == "__main__":
  application.run()
