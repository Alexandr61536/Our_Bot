import vk_api
import requests
import random
from vk_api.longpoll import VkLongPoll, VkEventType


def send_pic (token, user_id, message, path):
    vk = vk_api.VkApi(token=token)
    #longpoll = VkLongPoll(vk)
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(path)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.method("messages.send", {"user_id": user_id, "message": message, "attachment": attachment, "random_id": random.randint(0,100000)})