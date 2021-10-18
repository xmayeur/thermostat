from th_set_ctrl import SetCtrl
from th_set_schedule import SetSchedule
import json
from time import sleep

config = json.load(open('config.json', 'r'))
default_day = config['default_day']
default_night = config['default_night']
sc = SetCtrl(default_day, default_night)
ss = SetSchedule()
ss.show()
sc.show()

while True:
    if sc.updated:
        config['default_night'] = sc.night_temp
        config['default_day'] = sc.day_temp
        sc.updated = False
        json.dump(config, open('config.json', 'w'))
        print('updated')

    sleep(1)
