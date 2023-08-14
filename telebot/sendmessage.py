import requests
from .models import TeleSettings

def sendTelegram(tg_name, tg_phone):
    # Создаем переменную и берем объёкт по id 1

    settings = TeleSettings.objects.get(pk=1)

    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)

    api = 'https://api.telegram.org/bot'
    # Собираем ссылку-запрос с помощью конкотенации строк
    method = api + token + '/sendMessage'

    part_1 = text[0:text.find('{')]
    part_2 = text[text.find('}')+1:text.rfind('{')]
    part_3 = text[text.rfind('}'):-1]

    # Сконкотенируем все 3 части и присвоим в переменную, которую передадим в тело post-запроса
    text_slise = part_1 + tg_name + part_2 + tg_phone + part_3

    # формируем request-запрос
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise
    })
