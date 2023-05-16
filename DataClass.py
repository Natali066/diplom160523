#import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import community_token, acces_token
from core import VkBot


token = input('Token: vk1.a.dNojDDW48AEWikWCqn9pq8b4F5nL-D76wdCi4UOooav0kuXdsafTz797oqyOVgqxiD3oXTMWiZoE_YmQUgmcHeLLCiEMECDENFfuG8eZ5wo-WBIsTyqZVCxmtqt8ExuykoQnJl5gHtT8cD1dva49uCXkbiB0ENdpRvrb_Li6TfoqIvq9Hbmk02r4HE6HZDU_nMrVbfiqqllhtDsWZZqCxw')


vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


class VkBotInt():

	def _init_(self, community_yoken, acces_token):
		self.interface = vk_api.VkApi(token=community_token)
		self.api = VkTools(acces_token)
		self.params = None

	def message_send(self, user_id, message, attachment=None):
		self.interface.method('message.send’,
				{'user_id’: user_id,
				'message’: message,
				'attachment’: attachment,
				'random_id’: get_random_id()
				}
				)

	def event_handler(self):
		longpoll = VkLongPoll(self.interface)


		for event in longpoll.listen():
  			if event.type == VkEventType.MESSAGE_NEW and event.to_me:
				command = event.text.lower()

				if command == 'привет’:
					self.params = self.api.get_profile_info(event.user_id)
					self.message_send(event.user_id, f'здравствуй {self.params[“name”]}’)

				elif command == 'поиск’:
					users = self.api.serch_user(self.params)
					user = users.pop()
					photos_user = self.api.get_photos(user['id’])

				attachment = ' '
				for num, photo in enumerate(photos_user):
					attachment += f'photo{photo[“ower_id]}_{photo[“id”]}’
					if num == 2:
						break
				self.message_send(event.user_id, f'Встречайте {user[‘name’]}
						attachment=attachment
						)
				elif command == 'пока’:
					self.message_send(event.user_id, 'пока’)
				else:
					self.message_send(event.user_id, 'команда не опознана’)

if _name_ == '_main_’:
	bot = VkBotInt(community_token, acces_token)
	bot.event_handler()


        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
 coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
