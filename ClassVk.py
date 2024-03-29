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
                                          'count': 30,
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


    def get_photos(self, id):
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
        result.sort(key = lambda photo: photo['likes'] + photo['comments'])
        return result[:3]

    if __name__ == '__main__':
        # user_id = 219206692
        # tools = VkTools(acces_token)
        # params = tools.get_profile_info(user_id)
        # photos = tools.get_photos(worksheets['id'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
