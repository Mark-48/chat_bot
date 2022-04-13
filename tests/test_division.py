from chat import security_msg, get_name
import pytest
import requests
import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll

session = requests.Session()
vk_session = vk_api.VkApi(token="064e5aeb55fb8062b5c4db6859c1645785dc52df21bdb82867fbafbff4dcd5e6a45fdbb16473781658bf5")

longpoll = VkBotLongPoll(vk_session,181452959)
vk = vk_session.get_api()

def test_gate_name_user():
    with pytest.raises(TypeError):
        security_msg('Holla')

def test_gate_more_user():
        get_name("yandex")
        get_name(1)