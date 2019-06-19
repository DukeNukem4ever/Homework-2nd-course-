# -*- coding: utf-8 -*-
import flask
import telebot
import conf
import random
import re

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)

lis = []

with open('/home/DukeNukem4ever/mysite/1.txt','r',encoding = 'utf-8-sig') as text:
    lines = text.readlines()
    for line in lines:
        line = re.sub('\n','',line)
        line = re.sub('[,.?:!@"\']','',line)
        line = re.sub('[-—]',' ',line)
        if line != '' and line != '\n':
            lis.append(line)

random.shuffle(lis)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который отвечает на ваши реплики строчками из стихотворений Даниила Хармса.")
    bot.send_message(message.chat.id, "Пишите, пожалуйста, без знаков препинания. Я также могу проанализировать только слова, написанные на русском языке - без каких-либо цифр.")
    bot.send_message(message.chat.id, "Если Вы не получили от меня ответа, то попробуйте другое слово. Есть такие слова, к которым я не могу подобрать рифмы Хармса.")
    bot.send_message(message.chat.id, "Для полученя краткой информации о Данииле Хармсе введите /about.")


@bot.message_handler(commands=['about'])
def send_welcome2(message):
    bot.send_message(message.chat.id, "Даниил Иванович Хармс (настоящая фамилия Ювачёв) - советский писатель, поэт и драматург.")
    bot.send_message(message.chat.id, "Он известен благодаря своим детским стихотворениям, многие из которых были первоначально написаны при сотрудничестве с журналами 'Ёж', 'Чиж', 'Октябрята' и 'Сверчок', причём как самостоятельно, так и в тандемах с некоторыми писателями (такими, как Самуил Яковлевич Маршак).")
    bot.send_message(message.chat.id, "Хармс очень ответственно подходил к работе в детской литературе, которая в 30-х годах XX века была для него главным источником дохода.")
    bot.send_message(message.chat.id, "Это отличало его от таких любительских (по мнению общества) писателей, как Александр Введенский.")


@bot.message_handler(func=lambda m: True)  # этот обработчик реагирует все прочие сообщения
def send_len(message):
    need = []
    for line in lis:
        line = re.sub('\n','',line)
        line = re.sub('[,.?:;!@"\']','',line)
        line = re.sub('-',' ',line)
        line = re.sub('   ', '', line)
        if message.text[-3:] == line[-3:]:
            need.append(line)
            break
        else:
            continue
    if need != []:
        bot.send_message(message.chat.id, '{}'.format(line))
    else:
        bot.send_message(message.chat.id, 'Не могу подобрать рифму. Попробуйте ещё раз.')
    random.shuffle(lis)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
