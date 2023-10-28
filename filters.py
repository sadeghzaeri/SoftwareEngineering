from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(name="bot",
             api_id=x,
             api_hash="x",
             bot_token="x")
@app.on_message(filters.command("start"))
def start_command(client:Client, message:Message):
    message.reply_text("Finally u clicked on /start :)")

@app.on_message(filters.private & filters.text)
def reply_back(client:Client, message:Message):
    message.reply_text("هم توی دایرکتی هم تکست داری میدی.")

@app.on_message(filters.private & filters.sticker)
def reply_back(client:Client, message:Message):
    message.reply_text("هم توی دایرکتی هم استیکر داری میدی.")

@app.on_message(filters.private & filters.regex("به جدم"))
def reply_reg(client:Client, message:Message):
    message.reply_text("نیستی در حدم")
# @app.on_message()
app.run()