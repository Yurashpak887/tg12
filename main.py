import telebot
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("TOKEN")
name = os.getenv("NAME")
print(name)


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_message(message):
    text = message.text
    print(text, "команду яку зловив фільтр!")
    bot.send_message(message.chat.id, "Команду отримано!")


@bot.message_handler(commands=['hello'])
def hello_message(message):
    text = message.text
    print(text, "команду яку зловив фільтр!")
    bot.send_message(message.chat.id, "І тобі привіт!")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text == "Пайтон":
        bot.send_message(message.chat.id, "О це ти красавчик")
    else:
        bot.send_message(message.chat.id, "О це ти канєшно!")


print("Бот запущено")

bot.infinity_polling()