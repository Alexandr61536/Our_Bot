import vk_api
import requests
import random
import json
from vk_api.longpoll import VkLongPoll, VkEventType

import config

token=config.token
def send_pic (user_id, message, path):
    global token
    vk = vk_api.VkApi(token=token)
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(path)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.method("messages.send", {"user_id": user_id, "message": message, "attachment": attachment, "random_id": random.randint(0,100000)})

def textMessage(user_id, message):
    global token
    vk = vk_api.VkApi(token=token)
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(-2147483648, +2147483648) })
def SendKeyboard(user_id, text, keyboard):
    global token
    vk = vk_api.VkApi(token=token)
    vk.method('messages.send', {'user_id': user_id, 'message': text, 'keyboard': keyboard, "random_id": random.randint(-2147483648, +2147483648) })