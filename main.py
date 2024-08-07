import telebot

bot = telebot.TeleBot('7128466389:AAFrPvEcIuGkyQlKyCEEF0dE7Y4NvVqL9SQ')

# обрабатываем команду start
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'В контексте китайской культуры пион считается королевой цветов, и сопоставим со смыслом, который конкурирует в нашей культуре с розой.', parse_mode = 'Markdown')

@bot.message_handler(commands=['types_of_pionies'])
def main(message):
    bot.send_message(message.chat.id, '*Древовидный пион* — кустарники высотой до 2 метров с крепкими, почти одеревеневшими побегами и крупными цветами.\n*Травянистый пион* — более низкорослые растения с мягкими побегами.\n*Махровые пионы* — самые пышные бутоны диаметром до 25 см с тремя слоями лепестков.', parse_mode = 'Markdown')

@bot.message_handler(commands=['the_meaning_of_peonies'])
def main(message):
    bot.send_message(message.chat.id, '[Значение пионов в разных странах](https://sochi-cvetov.ru/articles/piony-simvolika-i-znachenie)', parse_mode = 'Markdown')

# проверка новых сообщений
bot.infinity_polling()

