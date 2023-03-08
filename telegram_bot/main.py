import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from nike import get_products_by_category

# токен для доступа к API бота
TOKEN = '6271458016:AAHrfmqvo2kSHQ9ODL5-JQNwA4lt07MVp5A'

# создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# создание кнопок выбора категории
category_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
category_buttons.add(KeyboardButton('Мужская обувь'))
category_buttons.add(KeyboardButton('Женская обувь'))
category_buttons.add(KeyboardButton('Детская обувь'))
category_buttons.add(KeyboardButton('New&featured'))


# обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # приветственное сообщение и кнопки выбора категории
    bot.send_message(message.chat.id, "Привет! Я бот, который поможет тебе найти нужную обувь на сайте Nike. "
                                      "Пожалуйста, выбери категорию:", reply_markup=category_buttons)

# обработчик выбора категории
@bot.message_handler(func=lambda message: message.text in ['Мужская обувь', 'Женская обувь', 'Детская обувь', 'New&featured'])
def handle_category_choice(message):
    # получаем категорию и отправляем список продуктов
    category = message.text.lower()
    products = get_products_by_category(category)
    bot.send_message(message.chat.id, f"Вот все продукты категории {category}:\n\n{products}")

# запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)



