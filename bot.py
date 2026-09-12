import telebot

# ⚠️ ЗАМЕНИ на свой токен из BotFather
BOT_TOKEN = "8963193595:AAFWvW2IKG5m_VuLaPL8tlHWpDdHHM_Zf-U"

# ⚠️ Имя файла с твоей картинкой (если назвал pic.jpg — оставь так)
IMAGE_PATH = "pic.png"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    # Открываем картинку и отправляем
    with open(IMAGE_PATH, "rb") as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Нажми /start")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()