import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import community_token, acces_token
from core import VkTools


token = input('Token: vk1.a.dNojDDW48AEWikWCqn9pq8b4F5nL-D76wdCi4UOooav0kuXdsafTz797oqyOVgqxiD3oXTMWiZoE_YmQUgmcHeLLCiEMECDENFfuG8eZ5wo-WBIsTyqZVCxmtqt8ExuykoQnJl5gHtT8cD1dva49uCXkbiB0ENdpRvrb_Li6TfoqIvq9Hbmk02r4HE6HZDU_nMrVbfiqqllhtDsWZZqCxw')

class BotInt():
    def __init__(self, comunity_token, acces_token):
        self.vk = vk_api.VkApi(token=comunity_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_tools = VkTools(acces_token)
        self.params = {}
        self.worksheets = []
        self.offset = 0

    def message_send(self, user_id, message, attachment=None):
        self.vk.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': get_random_id()}
                       )
    def event_handler(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'hi':
                    self.params = self.vk_tools.get_profale_info(event.user_id)
                    self.message_send(
                        event.user_ud, f'hi, {self.params["name"]}')
                elif event.text.lower() == 'search':
                    self.message_send(
                        event.user_id, 'start search')
                    if self.worksheets.pop()
                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:''
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
                    else:
                        self.worksheets = self.vk_tools.search_worksheet(
                            self.params, self.offset)

                        worksheet =  self.worksheets.pop()

                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:'id'
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
                        self.offset += 10

                    self.message_send(
                        event.user_id,
                        f'name: {worksheet["name"]} link: vk.com/{worksheet["id"]}',
                        attachment=photo_string
                    )
                elif event.text.lower() == 'by':
                     self.message_send(
                         event.user_id, 'by')

                else:
                     self.message_send(
                         event.user_id, 'unknown kommand')
    if __name__ == '__main__':
        bot_interface = BotInterface(comunity_token, acces_token)
        bot_interface.event_handler()

class BotInt():
    def __init__(self, comunity_token, acces_token):
        self.vk = vk_api.VkApi(token=comunity_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_tools = VkTools(acces_token)
        self.params = {}
        self.worksheets = []
        self.offset = 0

    def message_send(self, user_id, message, attachment=None):
        self.vk.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': get_random_id()}
                       )
    def event_handler(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'привет':
                    self.params = self.vk_tools.get_profale_info(event.user_id)
                    self.message_send(
                        event.user_ud, f'привет друг, {self.params["name"]}')
                elif event.text.lower() == 'поиск':
                    self.message_send(
                        event.user_id, 'Начинаем поиск')
                    if self.worksheets.pop()
                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:''
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]}',
                    else:
                        self.worksheets = self.vk_tools.search_worksheet(
                            self.params, self.offset)

                        worksheet =  self.worksheets.pop()

                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:'id'
                            photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
                        self.offset += 10

                    self.message_send(
                        event.user_id,
                        f'name: {worksheet["name"]} link: vk.com/{worksheet["id"]}',
                        attachment=photo_string
                    )
                elif event.text.lower() == 'by':
                     self.message_send(
                         event.user_id, 'by')

                else:
                     self.message_send(
                         event.user_id, 'unknown kommand')
    if __name__ == '__main__':
        bot_interface = BotInterface(comunity_token, acces_token)
        bot_interface.event_handler()
class VkTools():
    def __init__(self, acces_token):
       self.api = vk_api.VkApi(token=acces_token)
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

if _name_ == '_main_':
	bot = VkBotInt(community_token, acces_token)
	bot.event_handler()


coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
