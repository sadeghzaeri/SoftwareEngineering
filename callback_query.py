from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup,ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

app = Client(name="bot",
             api_id=x,
             api_hash="x",
             bot_token="x")

    #dokme shishe iii
@app.on_message(filters.command("haji"))
def start_command(client:Client, message:Message):
    message.reply_text("Finally u clicked on /start :)",reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Dokme1",callback_data="dokme"),InlineKeyboardButton(text="Dokme Link",url="x.com")]
        ]
    ))

@app.on_callback_query()
def call_q_handler(c:Client, callback:CallbackQuery):
    print(callback.from_user.id)
    #send id of user
    #has lots of methods.

@app.on_callback_query()
def call_q_handler(c:Client, callback:CallbackQuery):
    if callback.data == "salam":
        callback.message.reply_text("hello from Dokme 1")


# if callback.data == "salam":
# hazfesh ham hast to jalase 10 gofte shode, be vasile ReplyKeyboardRemove attribiut()
app.run()