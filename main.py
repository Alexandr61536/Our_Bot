import vk_api
import requests
import random
import json
from vk_api.longpoll import VkLongPoll, VkEventType

import diff_messages
import keyboards
import config

def ParseNumber (msg):
    corp= msg[0]
    floor= msg[2]
    num= msg[3:5]
    return {'corp': corp, 'floor': floor, 'num': num}

# API-ключ созданный ранее
token = config.token

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            '''
            if request == "картинка 1":
                diff_messages.send_pic(event.user_id, 'тестовая картинка 1', 'maps/gk/1.png')
            elif request == 'картинка 2':
                diff_messages.send_pic(event.user_id, 'тестовая картинка 2', 'maps/Bk/1.png')
            '''
                
            if (request.upper() == 'START') or (request.upper() == 'НАЧАТЬ'):
                diff_messages.textMessage(event.user_id, 'Напиши мне код кабинета в формате <Корпус>-<номер>, а я расскажу, как до него добраться')
            elif (len(request)==5) and ('-' in request):
                aim = ParseNumber(request)
                #Затычка, пока нет карт:
                diff_messages.textMessage(event.user_id, 'Вот, где корпус\nТипо скинул фото maps/'+aim['corp']+'_onmap')
                diff_messages.textMessage(event.user_id, 'Вот вход\nТипо скинул фото maps/'+aim['corp']+'_enter')
                ###
                '''
                diff_messages.send_pic(event.user_id, 'Вот, где корпус', 'maps/'+aim['corp']+'_onmap')
                diff_messages.send_pic(event.user_id, 'Вот вход', 'maps/'+aim['corp']+'_enter')
                '''
                diff_messages.SendKeyboard(event.user_id, 'Нажми на кнопку, как зайдёшь в корпус', keyboards.keyboard_enclosure)
                
            elif request=='Дошёл до корпуса':
                #Затычка, пока нет карт:
                diff_messages.textMessage(event.user_id, 'Вот где нужная тебе лестница, поднимись по ней на '+aim['floor']+' этаж\nТипо скинул фото maps/'+aim['corp']+'/'+aim['floor']+'_onmap')
                ###
                '''
                diff_messages.send_pic(event.user_id, 'Вот где нужная тебе лестница, поднимись по ней на '+aim['corp']+aim['floor']+' этаж', 'maps/'+aim['corp']+'/'+aim['floor']+'_onmap')
                '''
                diff_messages.SendKeyboard(event.user_id, 'Нажми на кнопку, как поднимешься', keyboards.keyboard_floor)
                
            elif request == 'Поднялся на этаж':
                #Затычка, пока нет карт:
                diff_messages.textMessage(event.user_id, 'Вот, где находится нужный тебе кабинет\nТипо скинул фото maps/'+aim['corp']+'/'+aim['floor']+'/'+aim['num']+'_onmap')
                ###
                '''
                diff_messages.send_pic(event.user_id, 'Вот, где находится нужный тебе кабинет', 'maps/'+aim['corp']+'/'+aim['floor']+'/'+aim['num']+'_onmap')
                '''

            