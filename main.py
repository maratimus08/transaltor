import json
import requests
import telebot


def translate(word):
    url = f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&text={word}&lang=pt-ru&dict=pt-ru.regular'
    response = requests.get(url=url)
    try:
        result = json.loads(response.text)["pt-ru"]['regular'][0]['tr'][0]['text']
    except Exception:
        return None
    return result


bot = telebot.TeleBot('7778838654:AAH2O2ur-pDT68aCeT3WFDOtt3lG1uaQEKw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ')


@bot.message_handler(content_types=['text'])
def text_message(message):
    bot.send_message(message.chat.id, translate(message.text))


bot.infinity_polling()
