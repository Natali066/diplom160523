import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import community_token, acces_token
from ClassVk import VkTools
from db import add_user, chek_user

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

                    if self.worksheets:
             
       
                    else:
                        self.worksheets = self.vk_tools.search_worksheet(
                            self.params, self.offset
                        )
                        self.offset += 30

                
                    worksheet = self.worksheets.pop()
                    while chek_user(event.user_id, worksheet['id']):
                        if  worksheet:
                            worksheet = self.worksheets.pop()
                        else:
                            self.worksheets = self.vk_tools.search_worksheet(
                                self.params, self.offset
                            )
                            self.offset += 30     
                    
                    
                    photos = self.vk_tools.get_photos(worksheet['id'])
                    photo_string = ''
                    for photo in photos:
                        photo_string += f'photo{photo["owner_id"]}_{photo["id"]},'
           
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



if __name__ == '_main_':
	bot = BotInt(community_token, acces_token)
	bot.event_handler()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
