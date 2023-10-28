from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(name="bot",
             api_id=x,
             api_hash="x",
             bot_token="x")

@app.on_message(filters.command("start"))
def start_command(client:Client, message:Message):
    message.reply_text("Finally u clicked on /start :)")

app.run()


# from pyrogram import Client, filters