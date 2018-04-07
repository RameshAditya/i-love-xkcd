import schedule
import time
from slackclient import SlackClient
import random
import xkcd
import datetime

def slack_message():
    
    token = 'YOUR_LEGACY_TOKEN'
    sc = SlackClient(token)

    #acquire past messages on desired channel
    history = sc.api_call("channels.history", channel = "CA2R3V1L5") #channel = "YOUR_CHANNEL_ID" (code to find, available below while loop)
    
    command = history['messages'][0]['text']
    if 'moar' in command:   #if user wants more comics
        
        #account for constantly increasing size of XKCD comics, and accordingly find random comic
        d1 = datetime.date(2012, 11, 6)
        now = datetime.datetime.now()
        d0 = datetime.date(now.year, now.month, now.day)
        upper = (d0 - d1).days
    
        rno = random.randint(1,upper)

        img_chosen = xkcd.Comic(rno)
        path = img_chosen.getImageLink()
    
        #push message to channel
        sc.api_call('chat.postMessage', channel = 'general',
                    text = path, username='XKCDbot',
                    icon_emoji = ':robot_face:')
        return 1 #success!
    return 0

#instantiate scheduler with task and rate
schedule.every(5).seconds.do(slack_message)

#execute task
while True:
    schedule.run_pending()
    time.sleep(1)


# Get Channel IDs using this snippet
    #trial = sc.api_call("channels.list")
    #trialchannels = trial['channels']
    #for i in trialchannels:
    #    print(i['name'] + "(" + i['id'] + ")")
