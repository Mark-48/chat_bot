import vk_api
import random
import sqlite3
import os
import time
import difflib as d
import requests
import string
import json
import platform
from vk_api import VkApi
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll

session = requests.Session()
vk_session = vk_api.VkApi(token="c4055a3d21b4b34934fb306bcfa23c69ed5c7f7820ae255f0cf90c3ecaf682acbd902a689d83aa3077202")

longpoll = VkBotLongPoll(vk_session,181452959)
vk = vk_session.get_api()

image = "D:/Program Files/programming/pythonProject/8lRtGJ0Cl9I.jpg"




def send_photo():
    while True:
        vk.messages.send(random_id=random.randint(1, 123456798901),chat_id=1, attachment='photo166034972_457263499' )
        time.sleep(10)

print('bot activated...')

while True:
    vk.messages.send(random_id=random.randint(1, 123456798901), chat_id=1, attachment='photo166034972_457263499')
    time.sleep(12600)

