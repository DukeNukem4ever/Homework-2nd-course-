# -*- coding: utf-8 -*-
import flask
import telebot
import conf
import random
import re

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)  # бесплатный аккаунт pythonanywhere запрещает работу с несколькими тредами

# удаляем предыдущие вебхуки, если они были
bot.remove_webhook()

# ставим новый вебхук = Слышь, если кто мне напишет, стукни сюда — url
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

# этот обработчик запускает функцию send_welcome, когда пользователь отправляет команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который отвечает на ваши реплики строчками из стихотворений Даниила Хармса.")
    bot.send_message(message.chat.id, "Пишите, пожалуйста, без знаков препинания.")
    bot.send_message(message.chat.id, "Если Вы не получили от меня ответа, то попробуйте другое слово. Есть такие слова, к которым я не могу подобрать рифмы Хармса.")


@bot.message_handler(func=lambda m: True)  # этот обработчик реагирует все прочие сообщения
def send_len(message):
    need = []
    for line in lis:
        line = re.sub('\n','',line)
        line = re.sub('[,.?:;!@"\']','',line)
        line = re.sub('-',' ',line)
        line = re.sub('   ', '', line)
        if message.text[-2:] == line[-2:]:
            need.append(line)
            break
        else:
            continue
    if need != []:
        bot.send_message(message.chat.id, '{}'.format(line))
    else:
        bot.send_message(message.chat.id, 'Не могу подобрать рифму. Попробуйте ещё раз.')
    random.shuffle(lis)


# пустая главная страничка для проверки
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

# обрабатываем вызовы вебхука = функция, которая запускается, когда к нам постучался телеграм
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
