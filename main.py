
# this program works fine
from pytube import YouTube
from pytube.innertube import _default_clients
# bot library 
from telebot import TeleBot,types,util
from telebot.types import*
from telebot.util import user_link

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

bot = TeleBot("6934289676:AAE0COsWQoMTj4TR6hZGbVvhAZqDlUVZvjw",parse_mode="HTML")

markup = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
markup.add(group,channel)

@bot.message_handler(commands=["start"])
def greet(msg):
    user = f"{user_link(msg.from_user)}"
    bot.reply_to(msg,f"""Hello {user} send youtube video url to get its thumbnail""",reply_markup=markup)


@bot.message_handler(func=lambda m:True)
def downloadAudio(msg):
    url = msg.text.strip()
    # create a youtube object
    yt = YouTube(url)
    thumbnail = yt.thumbnail_url
    print(f"Thumbnail url: {thumbnail}")
    bot.send_photo(msg.chat.id,thumbnail,reply_to_message_id=msg.message_id,reply_markup=markup)
  

bot.infinity_polling()
