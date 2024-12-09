import telebot

# Токен вашого бота
API_TOKEN = ''

# Створюємо бота
bot = telebot.TeleBot(API_TOKEN)

# Обробка команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Це бот!")
    
@bot.message_handler(func=lambda _: True)
def echo(message):
    bot.reply_to(message, message.text)

# Запускаємо бота
bot.infinity_polling()
