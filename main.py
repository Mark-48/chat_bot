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
from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll
PUTH="C:/Users/maksim/Desktop/програмирование/проекты/python/socialbot/DATA.db"

session = requests.Session()
vk_session = vk_api.VkApi(token="993562cdd1c83ef7657b596d944d14a3537b2b053c3cc30d84393a40cfd675aabadd39be192f41f0deaa3")

longpoll = VkBotLongPoll(vk_session,208523995)
vk = vk_session.get_api()

def req_ctoken():
    size = 8
    generate_cod = ''.join(random.choice(string.ascii_letters) for _ in range(size))
    cod_id = {'cod': generate_cod, 'user': str(user_id)}
    return cod_id

def check_user(b):
    conn = sqlite3.connect(PUTH)
    cursor = conn.cursor()
    sql='SELECT * FROM blog WHERE user_ID = "%s"'
    cursor.execute(sql%(b))
    bts = cursor.fetchall()
    print(bts)
    return bts

def gen_file():
    put = "C:/Users/maksim/Desktop/програмирование/проекты/python/cloud.bot/users/"
    path =put + str(cod_id['user'])
    uses = os.listdir(put)
    if cod_id['user'] in uses:
        mess_send('Enter this code in Desktop ' + "&#9773;")
        f = open(path + '/file.txt', 'w')
        f.write(cod_id['cod'])
        f.close()
    if cod_id['user'] not in uses:
        os.mkdir(path)
        f = open(path + '/file.txt', 'w')
        f.write(cod_id['cod'])
        f.close()


def mess_send(txt):
    vk.messages.send( random_id=random.randint(1,123456798901), user_id=user_id,message=txt)

def security_msg(txt):
    vk.messages.send(random_id=random.randint(1,1234567989),user_id=166034972,message=txt)
print('bot activated...')



while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
        #Слушаем longpoll, если пришло сообщение то:

            txt = event.object['text']
            user_id = event.obj['from_id']
            print('---------------')
            print(event.object)
            if event.obj['text'].lower() == 'cod' or event.obj['text'].lower() == 'код' or event.obj['text'].lower() == 'code':
                    size=8
                    generate_cod = ''.join(random.choice(string.ascii_letters) for _ in range(size))
                    cod_id = {'cod': generate_cod, 'user': str(user_id)}
                    ids = cod_id['cod']+'-'+cod_id['user']

                    mess_send("your code: "+ids)

                    print('user: '+str(user_id))

                    gen_file()
            if event.obj['text'].lower()=='перевод':
                mess_send('пашол нахуй чОрт')

            if event.obj['text'].lower()=='ctoken':
                eu = user_id
                a = req_ctoken()['cod']
                b = req_ctoken()['user']
                ids = a + '-' + b


                if len(check_user(user_id))==0:
                    all = (str(b), a)
                    conn = sqlite3.connect(PUTH)
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO blog VALUES (?,?)', all)
                    conn.commit()
                    conn.close()

                    mess_send('Welcome to the CLOUD.BOT')
                    mess_send('this your CToken(CloudToken): '+ids)
                    mess_send('Enter this code in Desktop '+ "&#9773;")

                else:
                    conn.close()
                    mess_send('Your away register in CLOUD.SYS: ')


            if event.obj['text'].lower()=='rename' or event.obj['text']=='upd' or event.obj['text'].lower()=='res':
                 a = req_ctoken()['cod']
                 id = req_ctoken()['user']
                 ids = a + '-' + id
                 all = (str(id), a)


                 if len(check_user(user_id))==0:
                     mess_send('your dont in SYS')
                     conn.close()
                 else:
                     conn.close()

                     connection = sqlite3.connect(PUTH, check_same_thread=False)
                     q = connection.cursor()

                     update="UPDATE blog SET token=? WHERE user_ID = ?"
                     q.execute(update,(a,id))
                     connection.commit()
                     connection.close()
                     mess_send('your new Ctoken: '+a)

            if txt.lower()=='del':
                 if len(check_user(user_id))==0:
                     mess_send('your dont in SYS')
                     conn.close()

                 else:
                     conn = sqlite3.connect(PUTH)
                     cursor = conn.cursor()
                     sql = 'DELETE FROM blog WHERE user_ID = "%s"'
                     cursor.execute(sql % (user_id))
                     mess_send('your removed from the Cloud.Bot')
                     conn.commit()
                     conn.close()
                     # you are removed from the database