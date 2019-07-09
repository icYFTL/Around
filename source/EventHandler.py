from source.APIWorker import APIWorker
from source.StaticMethods import StaticMethods


class EventHandler:
    def __init__(self, event):
        self.event = event
        self.api = APIWorker()
        self.user = None

    def allocate(self):
        try:
            repl = self.event.get('updates')[0][0]
            self.user = self.api.user_get(-self.event.get("updates")[0][1])
            if repl == 8:
                return self.online()
            elif repl == 9:
                return self.offline()
            else:
                return
        except:
            return

    def platform(self, platform_id):
        if platform_id == 1:
            return 'Веб-версия сайта'
        elif platform_id == 2:
            return 'Iphone'
        elif platform_id == 3:
            return 'Ipad'
        elif platform_id == 4:
            return 'Android'
        elif platform_id == 5:
            return 'Windows Phone'
        elif platform_id == 6:
            return 'Windows 8'
        else:
            return 'Полная версия сайта'

    def sex_checker(self, sex):
        if sex == 2:
            return ''
        return 'а'

    def randevu(self, data):
        return "({time}): {last} {first} стал{sex} {status}. Объект: {device}".format(time=data['time'],
                                                                                      last=data['last'],
                                                                                      first=data['first'],
                                                                                      sex=data['sex'],
                                                                                      status=data['status'],
                                                                                      device=data['device'])

    def offline(self):
        return self.randevu({'time': StaticMethods.get_time().strftime("%D | %T"),
                             'last': self.user.get("last_name"),
                             'first': self.user.get("first_name"),
                             'sex': self.sex_checker(self.user.get('sex')),
                             'status': 'оффлайн',
                             'device': self.platform(
                                 self.event.get('updates')[0][2] % 256)
                             })

    def online(self):
        return self.randevu({'time': StaticMethods.get_time().strftime("%D | %T"),
                             'last': self.user.get("last_name"),
                             'first': self.user.get("first_name"),
                             'sex': self.sex_checker(self.user.get('sex')),
                             'status': 'онлайн',
                             'device': self.platform(
                                 self.event.get('updates')[0][2] % 256)
                             })
