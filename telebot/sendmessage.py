import requests
from .models import TeleSettings

def sendTelegram(tg_name, tg_phone):
    # Проверим наличие данных объекта settings. Если их нет, то ничего не делать
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        # Собираем ссылку-запрос с помощью конкотенации строк
        method = api + token + '/sendMessage'
        # Т.к.text обязательное поле, то проведем проверку на наличие фигурных скобок в тексте. Если они все на месте, то разделяем текст на 3 части
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]
            # Сконкотенируем все 3 части и присвоим в переменную, которую передадим в тело post-запроса
            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slide = text
        try:
            # формируем request-запрос
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
                })
        # В слуае возникнования ошибки ничего не делаем
        except:
            pass
        # Отлавливаем ошибку
        finally:
            # Проверяем если сервер не ответил кодом "200", то ошибка наша
            if req.status_code != 200:
                print("Ошибка отправки")
            elif req.status_code == 500:
                print("Ошибка сервера 500")
            else:
                print("Сообщение успешно отправлено!")
    else:
        pass
