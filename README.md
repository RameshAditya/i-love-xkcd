# I :heart: XKCD
### A Slack App that shares an XKCD Comic upon request from a user on the channel
-----------------------------------------------

## What I :heart: XKCD is
I :heart: XKCD is a slack app that parses a channel's message **every 5 seconds** and upon finding an impending `moar` (slang for "more") request sends an XKCD comic directly to the channel, for laughs.

![](https://github.com/RameshAditya/i-love-xkcd/blob/master/sample.gif)


*To speed up the response time, you may change the frequency with which messages are checked and if you've got the bandwidth to spare, you can take it down to checking every second.*

*Additionally, you could also modify the `schedule()` method to send an image without waiting for a request, in daily or weekly or any kind of interval.*

## What it does
XKCD is a webcomic of "romance, sarcasm, math, and language" and is pretty geeky in general. This project leverages the XKCD python module, to retrieve an image and the Slack API to send the image onto a slack channel.

## Set up instructions
You'll need to modify this code to run for your slack channel should you desire so, and for which you'll need to find your channel id and replace it in the `slack_message()` function, in the line `history = sc.api_call("channels.history", channel = "YOUR_CHANNEL_ID")`

In order to do so, you may
* Resort to the large documentation (or)
* Check the commented snippet at the bottom of my implementation which I used to identify my channel ID

Your choice. :smile:

## How it works
After importing the required modules, the `slack_message()` function is where all the magic happens.

First, we initialize our token string with our legacy token obtained from the slack website (google "Slack Legacy Token" and acquire one for your app, and keep this secret)

Then you'll need to find your channel ID to replace the second parameter in the `history = sc.api_call("channels.history", channel = "YOUR_CHANNEL_ID")` function, which you can do by running the following snippet -

```
trial = sc.api_call("channels.list")
trialchannels = trial['channels']
for i in trialchannels:
     print(i['name'] + "(" + i['id'] + ")")
```
Once you find your channel ID and can correctly obtain the channel's history, identify the most recent message and check if it requests for an XKCD image.

If yes, retrieve a random XKCD image using their module (the date-time functions have been used to account for the constantly expanding rate of XKCD comics, for the implementation to "keep up with times")

And then use the Slack API to post the image. That's all! :smile:

Good luck!
