import requests
from .models import TeleSettings



token = '6559243464:AAFH0O4JnIZRBZzadOCLLdfQB-BYWtPU6xA'
chat_id = -912124557
text = "Test2"

def sendTelegram(tg_name, tg_phone):
    # Создаем переменную и берем объёкт по id 1

    settings = TeleSettings.objects.get(pk=1)

    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)

    api = 'https://api.telegram.org/bot'
    # Собираем ссылку-запрос с помощью конкотенации строк
    method = api + token + '/sendMessage'

    # Зададим переменную a и b, которые ищет первую правую и первую левую скобку
    a = text.find('{')
    b = text.find('}')

    # Зададим переменную c и b, которые ищет последнюю правую и последнюю левую скобку
    c = text.rfind('{')
    d = text.rfind('}')

    part_1 = text[0:a]
    part_2 = text[b+1:c]
    part_3 = text[d:-1]

    # Сконкотенируем все 3 части и присвоим в переменную, которую передадим в тело post-запроса
    text_slise = part_1 + tg_name + part_2 + tg_phone + part_3

    # формируем request-запрос
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise
    })
