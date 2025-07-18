import telebot
from config import TOKEN
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
bot = telebot.TeleBot(TOKEN)

def get_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Пластиковая бутылка', callback_data = 'btn1'))
    markup.add(InlineKeyboardButton('Кожура банана', callback_data = 'btn2'))
    markup.add(InlineKeyboardButton('Стекло', callback_data = 'btn3'))
    markup.add(InlineKeyboardButton('Аллюминиевая банка', callback_data = 'btn4'))
    markup.add(InlineKeyboardButton('Бумага', callback_data = 'btn5'))
    return markup
@bot.message_handler(commands=['start','help'])
def say_hello(message):
    bot.send_message(message.chat.id, 'Привет! Я бот по экологии')

@bot.message_handler(commands=['eco'])
def eco_items(message):
    bot.send_message(message.chat.id, 'Выбери предмет, про время разложения которого ты хочешь узнать', reply_markup = get_inline_keyboard())
@bot.callback_query_handler(func = lambda call: call.data in ['btn1','btn2','btn3','btn4','btn5'])
def handlen_inline_keyboard(call):
    items = {
        'btn1' : "450 лет",
        'btn2' : "до 2 лет",
        'btn3' : "более 1000 лет",
        'btn4' : "500 лет",
        'btn5' : "2 года",
    }
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, items[call.data])

bot.infinity_polling()