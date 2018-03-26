import os
from telethon import TelegramClient

api_id = os.environ['apiidWebHookSecretKey']
api_hash = os.environ['apihashWebHookSecretKey']

client = TelegramClient('session_name', api_id, api_hash)
client.start()
