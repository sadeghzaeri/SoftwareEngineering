from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup,ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

app = Client(name="bot",
             api_id=x,
             api_hash="x",
             bot_token="x")
@app.on_message(filters.command("start"))
def start_command(client:Client, message:Message):
    message.reply_text("Finally u clicked on /start :)",
                       reply_markup=ReplyKeyboardMarkup(
        [
            ['hello','bye'],
            ['khat 2']
        ]
                       ,resize_keyboard=True,one_time_keyboard=True,))
    #dokme shishe iii
@app.on_message(filters.command("haji"))
def start_command(client:Client, message:Message):
    message.reply_text("Finally u clicked on /start :)",reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Dokme1",callback_data="dokme"),InlineKeyboardButton(text="Dokme Link",url="x.com")]
        ]
    ))
@app.on_message()
def mess_handle(client:Client, message:Message):
    message.reply_chat_action("typing")
    message.reply_text("نوشتم")    
# hazfesh ham hast to jalase 10 gofte shode, be vasile ReplyKeyboardRemove attribiut()
app.run()