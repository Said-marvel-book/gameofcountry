import telebot
import os
from telebot import types
bot = telebot.TeleBot("1678843844:AAGgn-_HvA4aFmsKpSPQbFejDt5pUBjYBuY")
name = ""
chars = ""
gilds = ""
d = 0
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row("Союзы", "Атаки")
keyboard1.row("Защита", "Информация")
keyboard1.row("Настройки")
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row("Регистрация")
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row("Профиль", "Удалить аккаунт")
keyboard3.row("⬅️ Назад")
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard4.row("Новая атака", "Каталог атак")
keyboard4.row("⬅️ Назад")
keyboard5 = telebot.types.ReplyKeyboardMarkup()
keyboard5.row("Улучшить защиту", "Каталог защит")
keyboard5.row("⬅️ Назад")
@bot.message_handler(commands=["start"])
def start_message(message):
    global keyboard1, keyboard2
    try:
        r = open(f"{bot.get_chat(message.chat.id).username}.txt", "r", encoding="utf-8")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Привет, ты написал мне /start", reply_markup=keyboard1)
        r.close()
    except:
        bot.send_message(message.chat.id, "Привет, ты написал мне /start", reply_markup=keyboard2)
@bot.message_handler(commands=["gild"])
def gild_message(message):
    try:
       r = open(f"{bot.get_chat(message.chat.id).username}.txt", "r", encoding="utf-8")
    except:
        bot.send_message(message.chat.id, "Зарегайтесь")
        register(message)
    try:
        gilds = r.readline()
        gilds = r.readline()
        gilds = r.readline()
    except:
        bot.send_message(message.chat.id, "У Вас пока нет союзов")
    if gilds == "":
        bot.send_message(message.chat.id, "У Вас пока нет союзов")
        r.close()
    else:
        r.close()
        keyboard = telebot.types.ReplyKeyboardMarkup()
        for i in gilds.split(","):
            keyboard.row(i)
        keyboard.row("⬅️ Назад")
        bot.send_message(message.chat.id, f"Вы состоите в {gilds}", reply_markup=keyboard)
@bot.message_handler(content_types=["text"])
def send_text(message):
    global keyboard1, keyboard3, gilds, keyboard4, keyboard5, d
    try:
        r = open(f"{bot.get_chat(message.chat.id).username}.txt", "r", encoding="utf-8")
        gilds = r.readline()
        gilds = r.readline()
        gilds = r.readline().replace("\n", "")
        gilds = gilds.split(",")
    except FileNotFoundError:
        register(message)
    if message.text.lower() == "союзы":
        gild_message(message)
        f = open(f"{bot.get_chat(message.chat.id).username}.txt", "r+", encoding="utf-8")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if "state" not in i:
                f.write(i)
        f.truncate()
        f.write("\nstate1")
        f.close()
    elif message.text.lower() == "профиль":
        r = open(f"{bot.get_chat(message.chat.id).username}.txt", "r", encoding="utf-8")
        country = r.readline()
        chars = r.readline()
        chars = chars.split(",")
        charism = chars[0]
        treasure = chars[1]
        army = chars[2]
        trick = chars[3]
        atribute = chars[4]
        bot.send_message(message.chat.id, f"Страна: {country}\nХаризма: {charism}\nБогатство: {treasure}\nВоенная сила: {army}\nХитрость: {trick}\nАтрибуты: {atribute}")
        r.close()
    elif message.text.lower() == "регистрация":
        register(message)
    elif message.text.lower() == "настройки":
        bot.send_message(message.chat.id, "Настроим всё😉", reply_markup=keyboard3)
        f = open(f"{bot.get_chat(message.chat.id).username}.txt", "r+", encoding="utf-8")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if "state" not in i:
                f.write(i)
        f.truncate()
        f.write("\nstate1")
        f.close()
    elif message.text.lower() == "удалить аккаунт":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Да", callback_data="yesdel")
        keyboard.add(key_yes)
key_no = types.InlineKeyboardButton(text="Нет", callback_data="nodel")
        keyboard.add(key_no)
        bot.send_message(message.chat.id, text="Удалить аккаунт?", reply_markup=keyboard)
    elif message.text.upper() in gilds:
        r = open(f"{message.text}.txt", "r", encoding="utf-8")
        memb = r.readline()
        bot.send_message(message.chat.id, f"В союзе {message.text.upper()} состоят {memb}")
        r.close()
    elif message.text.lower() == "атаки":
        bot.send_message(message.chat.id, "Ваши атаки", reply_markup=keyboard4)
        f = open(f"{bot.get_chat(message.chat.id).username}.txt", "r+", encoding="utf-8")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if "state" not in i:
                f.write(i)
        f.truncate()
        f.write("\nstate1")
        f.close()
    elif message.text.lower() == "защита":
        bot.send_message(message.chat.id, "Ваша защита", reply_markup=keyboard5)
        f = open(f"{bot.get_chat(message.chat.id).username}.txt", "r+", encoding="utf-8")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if "state" not in i:
                f.write(i)
        f.truncate()
        f.write("\nstate1")
        f.close()
    elif message.text.lower() == "⬅️ назад":
        r = open(f"{bot.get_chat(message.chat.id).username}.txt", "r", encoding="utf-8")
        r = r.readlines()
        for i in r:
            if "state" not in i:
                pass
            else:
                d = int(i.replace("state", ""))
                break
        if d == 1:
            bot.send_message(message.chat.id, "Назад так назад", reply_markup=keyboard1)
        elif d == 3:
            bot.send_message(message.chat.id, "Назад так назад", reply_markup=keyboard3)
        elif d == 4:
            bot.send_message(message.chat.id, "Назад так назад", reply_markup=keyboard4)
        elif d == 5:
            bot.send_message(message.chat.id, "Назад так назад", reply_markup=keyboard5)
def register(message):
    bot.send_message(message.chat.id, "Название вашей страны")
    bot.register_next_step_handler(message, reg_chars)
def reg_chars(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, "Вот 5 характеристик. Харизма у народа, Богатство, Военная сила, Хитрость(стратегия, смекалка) и доп. атрибуты (транспорт,оружие,учёные). Напиши их значения через запятую их сумма должна быть равна 25. Максимальное значение характеристики 10.")
    bot.register_next_step_handler(message, reg_gilds)
def reg_gilds(message):
    global chars
    chars = message.text
    sum = 0
    for i in message.text.split(","):
        sum += int(i)
    if sum != 25:
        bot.send_message(message.chat.id, "Вот 5 характеристик. Харизма у народа, Богатство, Военная сила, Хитрость(стратегия, смекалка) и доп. атрибуты (транспорт,оружие,учёные). Напиши их значения через запятую их сумма должна быть равна 25. Максимальное значение характеристики 10.")
        bot.register_next_step_handler(message, reg_gilds)
    else:
        bot.send_message(message.chat.id, "Есть у вас пожелания в какие cоюзы, вы хотите вступить?")
        bot.register_next_step_handler(message, endreg)
def endreg(message):
    global gilds, keyboard1
    gilds = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data="yesreg")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data="noreg")
    keyboard.add(key_no)
    question = f"Вы {name}"
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global name, chars, gilds, keyboard1, keyboard2
    if call.data == "yesreg":
        r = open(f"{bot.get_chat(call.message.chat.id).username}.txt", "w", encoding="utf-8")
        r.write(name+"\n")
        r.write(chars+"\n")
        r.write(gilds+"\n")
        r.close()
        bot.send_message(call.message.chat.id, "Вы зарегались", reply_markup=keyboard1)
elif call.data == "noreg":
        register(call.message)
    elif call.data == "yesdel":
        os.remove(f"{bot.get_chat(call.message.chat.id).username}.txt")
        bot.send_message(call.message.chat.id, "К огромному сожалению ваш аккаунт удален", reply_markup=keyboard2)
    elif call.data == "nodel":
        bot.send_message(call.message.chat.id, "Ну и слава богу!")
bot.remove_webhook()
bot.polling()