from datatime import datatime
import vk_api
from config import acces_token

class VkBot():
	def _init_(self, acces_token):
		self.api = vk_api.VkApi(token=acces_token)
GROUP_ID = '219206692'

#берет профиль пользователя
def get_profile_user(self, user_id):
	info = self.api.method('users.get',
			{'user_id': user_id,
			'fields': 'city, bdate, sex, relation, home_town, age'
			}
			)

	user_info = {'name': info['first_name'] + ' '+ info['last_name'],
		'id': info['id'],
		'bdate': info['bdate'] if 'bdate' in info else None,
		'home_town': info['home_town'],
		'sex': info['sex'],
		'city': info['city']['id'],
		'age': info['age']
		}
	return  user_info

#ищет пользователя
def serch_users(self, params):

	sex = 1 if params['sex'] == 2 else 2
	city = params['city']
	now_year = datetime.now().year
	user_year = int(params['bdate'].split('.')[2])
	age = now_year – user_year
	age_from = age -2
	age_to = age =+2

	users = self.api.method('users.search',
			{'count': 10,
			'offset': 0,
			'age_from': age_from,
			'age_to': age_to,
			'sex': sex,
			'city': city,
			'status': 6,
			'id_closed': False
			}
			)
	try:
		users = user['items']
	except KeyError:
		return []

	res = []

	for user in users:
		if user['id_closed'] == False:
			res.append({'id': user['id'],
			'name': user['first_name'] + ' ' + user['last_name']
			}
			)

	return res

#берет фото
def get_photos(self, user_id):
	photos = self.api.method('photos.get',
			{'user_id': user_id,
			'album_id': 'profile',
			'extanded': 1
			}
			)

	try:
		photos = photos['items']
	exept KeyError:
		return []

	res = []

	for photo in photos:
		res.append({'owner_id': photo['owner_id'],
			'id': photo['id'],
			'likes': photo['likes']['count'],
			'comments': photo['comments']['count'],
			}
			)

	res.sort(key=lambda x: x['likes']+x['comments']*10, reverse = True

	return res

if _name_ == '_main_':
	bot = VkBot(acces_token)
	params = bot.get_profile_info(219206692)
	users = bot.serch_users(params)
	print(bot.get_photos(users[2]['id']))
				      
def get_settings_smart (self, user_id: VKUser):
        if not self.db.get_settings(vk_user):
            vk_user.set_default_settings()
            self.db.set_settings(vk_user)

# coding=utf-8
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
