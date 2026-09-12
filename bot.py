import telebot

# ⚠️ ЗАМЕНИ на свой токен из BotFather
# Было: BOT_TOKEN = "ваш_длинный_токен"
# Станет:
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ⚠️ Имя файла с твоей картинкой (если назвал pic.jpg — оставь так)
IMAGE_PATH = "pic.png"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    with open(IMAGE_PATH, "rb") as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Нажми /start")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
    