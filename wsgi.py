from telethon import TelegramClient
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    #print(client.get_me().stringify())
    client.send_message('@bot', 'Diesel')

    return "Hello World!"
    
if __name__ == "__main__":
application.run()
