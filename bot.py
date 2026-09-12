import os
import telebot
from dotenv import load_dotenv

load_dotenv()  # ← читает файл .env и подставляет значения в os.environ

BOT_TOKEN = os.getenv("BOT_TOKEN")
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
    