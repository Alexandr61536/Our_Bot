from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

def get_button (label, color, payload=" "):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard_enclosure = {
    "one_time": True,
    "buttons": [
    [get_button(label="Дошёл до корпуса", color="positive")]
    ]
}
keyboard_enclosure = json.dumps(keyboard_enclosure, ensure_ascii=False).encode('utf-8')
keyboard_enclosure = str(keyboard_enclosure.decode('utf-8'))

keyboard_floor = {
    "one_time": True,
    "buttons": [
    [get_button(label="Поднялся на этаж", color="positive")],
    ]
}
keyboard_floor = json.dumps(keyboard_floor, ensure_ascii=False).encode('utf-8')
keyboard_floor = str(keyboard_floor.decode('utf-8'))