from pyrogram import Client
from pyrogram.types import Message

app = Client(name="bot",
             api_id=x,
             api_hash="x",
             bot_token="x"

@app.on_message()
def reply_back(client:Client, message:Message):
    message.reply_text(message.text)

app.run()
#send what u send
#done