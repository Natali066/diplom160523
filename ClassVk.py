from pprint import pprint
from datetime import datetime
import vk_api
from vk_api.exceptions import ApiError
from config import acces_token


class VkTools:
    def __init__(self, acces_token):
        self.vkapi = vk_api.VkApi(token=acces_token)

    def _bdate_(self,bdate):
        user_year = bdate.split('.')[2]
        now = datetime.now().year
        return now - int(user_year)

    def get_profile(self,user_id):

        try:
            info, = self.vkapi.method('user.get',
                                      {'user_id': user_id,
                                       'fields': 'city, sex, relation, bdate'
                                       }
                                      )
        except ApiError as e:
            info = {}
            print(f'error = {e}')

        result = {'name': (info['first_name'] + ' ' + info['last_name']) if
                  'first_name' in info and 'last_name' in info else None,
                  'sex': info.get('sex'),
                  'city': info.get('city')['title'] if info.get('city') is not None else None,
                  'year': self._bdate_toyear(info.get('bdate'))
                  }
        return result

    def search_worksheet(selfself,params,offset):
        try:
            users = self.vkapi.method('user.search',
                                      {
                                          'count': 10,
                                          'offset': offset,
                                          'hometown': params['city'],
                                          'sex': 1 if params['sex'] == 2 else 2,
                                          'has_photo': True,
                                          'age_from': params['year'] - 2,
                                          'age_to': params['year'] + 2,
                                      }
                                      )
        except ApiError as e:
            users = []
            print(f'error = {e}')

        result = [{'name': item['first_name'] + item['last_name'],
                   'id': item['id']
                   } for item in users['items'] if item['is_closed'] is False
                  ]

        return result


    def get_photos (self, id):
        try:
            photos = self.vkapi.method('photos.get',
                                       {'owner_id': id,
                                        'album_id': 'profile',
                                        'extended': 1
                                        }
                                       )
        except ApiError as e:
            photos = {}
            print(f'error = {e}')

        result = [{'owner_id': item['owner_id'],
                   'id': item['id'],
                   'likes': item['likes']['count'],
                   'comments': item['comments']['count']
                   } for item in photos['items']
                  ]
        return result[:3]

    if __name__ == '__main__':
        user_id = 219206692
        tools = VkTools(acces_token)
        params = tools.get_profile_info(user_id)
        photos = tools.get_photos(worksheets['id'])


add_user(user_id, result[i][3], result[i][1], result[i][0], city, result[i][2], current_user_id.id)

	elif command == 'поиск':
		if len(self.users) == 0:
			self.users = self.api.serch_user(self.params)
					
	user = self.users.pop()

def check_db_master(user):
    current_user_id = session.query(user).filter_by(vk_id=ids).first()
    return current_user_id

	      
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
