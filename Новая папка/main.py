# pip install pytelegrambotapi

import telebot

bot = telebot.TeleBot("8743179683:AAG-zx2q8k8OKW1fPa4GnrDq7ejnDI46hvg")

@bot.message_handler(commands=["start"])
def boshlash(message):
    bot.reply_to(message, text="salom botimizga xush kelibsiz!!!")

@bot.message_handler(commands=["yordam"])
def yordam_f(message):
    bot.send_message(message.chat.id, text="sizga qanday yordam bera olaman!!!")

@bot.message_handler(commands=["rasm"])
def rasm_f(message):
    bot.send_photo(
        message.chat.id,
        photo="https://images.wallpaperscraft.ru/image/single/gora_skala_oblaka_1247254_1920x1080.jpg"
    )

@bot.message_handler(commands=["audio"])
def audio_f(message):
    with open("fff.mp3", "rb") as music:
        bot.send_voice(message.chat.id, voice=music)

print("working...")
bot.infinity_polling()