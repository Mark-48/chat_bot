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
import json
import requests

session = requests.Session()
vk_session = vk_api.VkApi(token="064e5aeb55fb8062b5c4db6859c1645785dc52df21bdb82867fbafbff4dcd5e6a45fdbb16473781658bf5")

longpoll = VkBotLongPoll(vk_session,181452959)
vk = vk_session.get_api()

image = "D:/Program Files/programming/pythonProject/8lRtGJ0Cl9I.jpg"


#!/usr/bin/python





def send_photo():
    while True:
        vk.messages.send(random_id=random.randint(1, 123456798901),user_id=user_id, attachment='photo166034972_457263499' )
        time.sleep(10)

def send_photo_mem(photoid):
        vk.messages.send(random_id=random.randint(1, 123456798901), chat_id=id, attachment=photoid)

def get_name(from_id):
  info = vk.users.get(user_ids = from_id)[0]
  full_name = info.get('first_name')
  return full_name

def send_sticker(st_id):
    vk.messages.send(random_id=random.randint(1, 123456798901), sticker_id=st_id, chat_id=id)

def mess_send(txt):

    vk.messages.send( random_id=random.randint(1,123456798901), user_id=user_id,message=txt, chat_id=id)

def chat_mess_send(txt):
    vk.messages.send(random_id=random.randint(1, 123456798901),  message=txt, chat_id=id)


def security_msg(txt):
    vk.messages.send(random_id=random.randint(1,1234567989),user_id=166034972,message=txt)
print('bot activated...')



while True:

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:

                txt=event.object['text']
                user_id=event.obj['from_id']

                print('---------------')
                print(event.object)

                if event.obj['text']:

                        word_sticker = event.obj['text'].lower().split()

                        for word in word_sticker:

                            if word == 'туц':
                                id = event.chat_id
                                send_sticker(13918)

                            else :
                                break
                try:

                        if event.obj['text'].lower() == 'ниггер':
                            id = event.chat_id
                            chat_mess_send('асуждаю, ' + get_name(event.obj['from_id']))
                            send_photo_mem('video365511761_456239070')

                        if event.obj['text'].lower() == '!бот':
                            id = event.chat_id
                            chat_mess_send('бот реагирует на такие слова: да, он лох, вы лохи, ниггер, так')
                            chat_mess_send('так же бот реагирует на ваши фото и записи со стены, и на стикеры так \n обновление от 03.03.2022 ')

                        if event.obj['text'].lower()=='вы лохи':
                            id = event.chat_id
                            print(id)
                            chat_mess_send("ахуел, сам такой")

                        if event.obj['text'].lower() == 'так':
                            id = event.chat_id
                            send_sticker(15292)

                        if event.obj['text'].lower() == 'егорка':
                            id = event.chat_id
                            chat_mess_send('https://vk.com/aifon4ikww')

                        if event.obj['text'].lower() == 'юрка' or event.obj['text'].lower() == 'великий туту':
                            id = event.chat_id
                            chat_mess_send('https://vk.com/tyty.blet2')

                        if event.obj['text'].lower() == 'макимка' :
                            id = event.chat_id
                            chat_mess_send('https://vk.com/playersuknowns')

                        if event.obj['text'].lower()=='он лох':
                            id = event.chat_id
                            print(id)
                            chat_mess_send("не, ну тут даже я согласен")
                            chat_mess_send("та еще сволочь")

                        elif event.obj['text'].lower() == 'егорка':
                            id = event.chat_id
                            send_sticker(65965)

                        elif event.obj['text'].lower() == 'димка':
                            id = event.chat_id
                            chat_mess_send('и')

                        elif event.obj['text'].lower() == 'тут':
                            id = event.chat_id
                            chat_mess_send('ТУТу')

                        elif event.obj['text'].lower() == 'туту':
                            id = event.chat_id
                            chat_mess_send('卐卐卐卐卐卐卐卐卐卐卐卐')
                            chat_mess_send('ой')

                        elif event.obj['text'].lower() == 'дискорд' or event.obj['text'].lower() == 'бебра' :
                            id = event.chat_id
                            chat_mess_send('ого, как ты узнал!!? во, держи - https://discord.gg/MeXpc2nT')

                        if event.obj['text'].lower()=='да':
                            id = event.chat_id
                            send_photo_mem('photo-178284437_457239477')

                        elif event.obj['attachments'][0]['type'] == 'photo':

                            id = event.chat_id
                            send_sticker(51590)

                        elif event.obj['attachments'][0]['type'] == 'wall':
                            id = event.chat_id
                            send_sticker(51578)

                        elif event.obj['attachments'][0]['type'] == 'sticker':

                            if event.obj['attachments'][0]['sticker']['sticker_id'] == 15292 or event.obj['attachments'][0]['sticker']['sticker_id'] == 57714 or event.obj['attachments'][0]['sticker']['sticker_id'] == 65756 :

                                print(event.obj['attachments'][0]['sticker']['sticker_id'])
                                id = event.chat_id
                                send_sticker(15292)

                        elif event.obj['text'].lower()=='ого':

                            id = event.chat_id
                            chat_mess_send('ага')

                        elif event.obj['text'].lower() == 'ага':

                            id = event.chat_id
                            chat_mess_send('в жопе нога')

                except:
                            print("Error!")
