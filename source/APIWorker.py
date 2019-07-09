from Config import Config
import vk_api
import requests
import json

from source.StaticData import StaticData


class APIWorker:
    def __init__(self):
        self.vk = vk_api.VkApi(token=Config.user_vk_access_token)

    def get_longpoll_server(self):
        return self.vk.method("messages.getLongPollServer", {'need_pts': 1})

    def user_get(self, user_id):
        return self.vk.method("users.get", {'user_ids': user_id, 'fields': 'sex'})[0]

    async def get_events(self):
        while True:
            l_serv = self.get_longpoll_server()
            data = json.loads(requests.get(
                "https://{}?act=a_check&key={}&ts={}&wait=25&mode=2&version=2".format(l_serv.get('server'),
                                                                                      l_serv.get('key'),
                                                                                      l_serv.get(
                                                                                          'ts'))).content.decode(
                'utf-8').replace("\r\n", ""))
            if 'failed' in data:
                l_serv = self.get_longpoll_server()
                continue
            StaticData.stack.append(data)
            l_serv = self.get_longpoll_server()
            StaticData.trigger.set()
