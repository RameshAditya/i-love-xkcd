import schedule
import time
from slackclient import SlackClient
import random
import xkcd
import datetime
#ob = xkcd.Comic(5)

h=[]
def slack_message():
    global h

    token = ''
    sc = SlackClient(token)

    history = sc.api_call("channels.history", channel = "CA2R3V1L5")
    #print(history)
    h = history
    command = history['messages'][0]['text']
    if 'moar' in command:
        d1 = datetime.date(2012, 11, 6)
        now = datetime.datetime.now()
        d0 = datetime.date(now.year, now.month, now.day)
        upper = (d0 - d1).days
    
        rno = random.randint(1,upper)

        img_chosen = xkcd.Comic(rno)
        path = img_chosen.getImageLink()
    
        sc.api_call('chat.postMessage', channel = 'general',
                    text = path, username='XKCDbot',
                    icon_emoji = ':robot_face:')
        return 1
    return 0


#def task():
#    print(1)
    
schedule.every(5).seconds.do(slack_message)

while True:
    schedule.run_pending()
    time.sleep(1)


# Get Channel IDs using this
    #trial = sc.api_call("channels.list")
    #trialchannels = trial['channels']
    #for i in trialchannels:
    #    print(i['name'] + "(" + i['id'] + ")")
