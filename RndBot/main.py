import telebot, random, sqlite3
import time
A = ["🪨", "✂️", "📝"]
C = []

connection = sqlite3.connect("users.db")
cursor_object = connection.execute(
  """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        win INTEGER,
        fail INTEGER,
        draw INTEGER
    )
  """
)
connection.close()
#_______________________________________________________________________________________
def win(username):
    print(username)
    connection = sqlite3.connect("users.db")

    cursor_object = connection.execute(
    f"""
        UPDATE users
        SET win = win+1
        WHERE name = "{username}"
    """
    )
    connection.commit()
    connection.close()
def fail(username):
    print(username)
    connection = sqlite3.connect("users.db")

    cursor_object = connection.execute(
    f"""
        UPDATE users
        SET fail=fail+1
        WHERE name = "{username}"
    """
    )
    connection.commit()
    connection.close()
def draw(username):
    
    connection = sqlite3.connect("users.db")
    print(username)
    cursor_object = connection.execute(
    
    f"""
        UPDATE users
        SET draw = draw+1
        WHERE name = "{username}"
    """
    )
    connection.commit()
    connection.close()
#_______________________________________________________________________________________
TOKEN = '7738805870:AAGk3ortTT3dQISXxDmhlJim0mpzVKxdM6Y'
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = telebot.types.KeyboardButton('Сыграть в 🪨✂️📝')
button_2 = telebot.types.KeyboardButton('Бросить кубик🎲')
keyboard.add(button_1, button_2)
#__________________________________________________________________________________________________________________


@bot.message_handler(commands=['start'])
def handle_start(message):
    global username
    bot.send_message(message.chat.id, 'Выберете действие снизу⬇️', reply_markup=keyboard)
    
    username = message.from_user.id
    C.append(username)
    
    connection = sqlite3.connect("users.db")
    cursor_object = connection.execute(
    f"""
        SELECT name
        FROM users
        WHERE name = {username}
    """
    )
    D = 0
    for obj in cursor_object.fetchall():
        D = D + 1
    if D > 0:
        pass
    else:
        cursor_object = connection.execute(
        f"""
            INSERT INTO users(name, win, fail, draw) 
            VALUES ('{message.from_user.id}', 0, 0, 0)
        """
        )
    username = "NULL"
    
    connection.commit() # команда для сохранения изменений в БД
    connection.close()

@bot.message_handler(func=lambda m: m.text.strip().capitalize() == 'Сыграть в 🪨✂️📝')
def command(message: telebot.types.Message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton('🪨', callback_data="🪨")
    button_2 = telebot.types.InlineKeyboardButton('✂️', callback_data="✂️")
    button_3 = telebot.types.InlineKeyboardButton('📝', callback_data="📝")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выберете предмет', reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text.strip().capitalize() == 'Бросить кубик🎲')
def command1(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Бросаю куб для бота🤖')
    bot.send_dice(message.chat.id, '')
    bot.send_message(message.chat.id, f'Бросаю куб для {message.chat.username}👽')
    bot.send_dice(message.chat.id, '')



@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    username = C[0]
    C.__delitem__
    if callback.data == '🪨':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        B = random.randint(0,2)
        bot.send_message(callback.message.chat.id, A[B])
        if B == 0:
            bot.send_message(callback.message.chat.id, 'Ничья', reply_markup=keyboard)
            draw(username)
        elif B == 1:
            bot.send_message(callback.message.chat.id, 'Вы выиграли', reply_markup=keyboard)
            win(username)
        elif B == 2:
            bot.send_message(callback.message.chat.id, 'Вы проиграли', reply_markup=keyboard)
            fail(username)
    elif callback.data == '✂️':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        B = random.randint(0,2)
        bot.send_message(callback.message.chat.id, A[B])
        if B == 1:
            bot.send_message(callback.message.chat.id, 'Ничья', reply_markup=keyboard)
            draw(username)
        elif B == 2:
            bot.send_message(callback.message.chat.id, 'Вы выиграли', reply_markup=keyboard)
            win(username)
        elif B == 0:
            bot.send_message(callback.message.chat.id, 'Вы проиграли', reply_markup=keyboard)
            fail(username)
    elif callback.data == '📝':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        B = random.randint(0,2)
        bot.send_message(callback.message.chat.id, A[B])
        if B == 2:
            bot.send_message(callback.message.chat.id, 'Ничья', reply_markup=keyboard)
            draw(username)
        elif B == 0:
            bot.send_message(callback.message.chat.id, 'Вы выиграли', reply_markup=keyboard)
            win(username)
        elif B == 1:
            bot.send_message(callback.message.chat.id, 'Вы проиграли', reply_markup=keyboard)
            fail(username)
    elif callback.data == "Сыграть в 🪨✂️📝":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('🪨', callback_data="🪨")
        button_2 = telebot.types.InlineKeyboardButton('✂️', callback_data="✂️")
        button_3 = telebot.types.InlineKeyboardButton('📝', callback_data="📝")
        keyboard.add(button_1, button_2, button_3)
        bot.send_message(callback.message.chat.id, 'Выберете предмет', reply_markup=keyboard)
    elif callback.data == "Бросить кубик🎲":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, f'Бросаю куб для бота🤖')
        bot.send_dice(callback.message.chat.id, '')
        bot.send_message(callback.message.chat.id, f'Бросаю куб для {callback.message.chat.username}👽')
        bot.send_dice(callback.message.chat.id, '')


print("Сервер запущен!")        
bot.polling(
    non_stop=True,
    interval=1 
)