# pyMessengerBotAPI
A Simple Python Wrapper for Messenger Bot API

##Requirements
1. This API is tested with Python 2.7
2. A token from the app you will create on [Developers Page](https://developers.facebook.com/apps/)
3. Flask should be installed
4. A webhook to receive messages. I used [ngrok](https://ngrok.com/download) for this.

##Writing your first bot
###Before proceeding further please go through the [documentation on developers page](https://developers.facebook.com/docs/messenger-platform/quickstart)

A template main.py is provided in messenger folder. You should use that as your bot page.

###Simple Echo Bot

<img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xfp1/t39.2365-6/13466933_1565510967084335_135574073_n.png" alt="screenshot" width="250" height="450"> 

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  
  bot.send_message(sender,"Welcome to Peter's Hats, what are you looking for today?")
```

###Using Buttons
####send_button_message(sender, text,buttons,metadata=None,quick_reply=None)
#####create_buttons(type,title,payload=None,url=None)

<img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xtp1/t39.2365-6/13509162_1732711383655205_1306472501_n.png" alt="screenshot" width="250" height="450"> 

```
def process_message(data):              
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  text = data['entry'][0]['messaging'][0]['message']['text']
  
  button1 = bot.create_button("web_url","Show Website",url="http://google.com")
  button2 = bot.create_button("postback","Start Chatting",payload="test123")
  
  bot.send_button_message(sender,"What do you want to do next?",[button1,button2])
```

###Using Generic Messages
####send_generic(sender, elements,metadata=None,quick_reply=None):
#####create_element(title,item_url=None,image=None,subtitle=None,buttons=[])

<img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xft1/t39.2365-6/13509251_1026555627430343_1803381600_n.png" alt="screenshot" width="250" height="450"> 

```
def process_message(data):              
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  text = data['entry'][0]['messaging'][0]['message']['text']
  
  button1 = bot.create_button("web_url","hello",url="http://google.com")
  button2 = bot.create_button("postback","test",payload="test123")
  title1 = "Welcome to Peter's Hats!"
  image1 = "http://xyz.png"
  subtitle1 = "We've got the right hat for everyone"
  
  element1 = bot.create_element("Test1",image=image1,subtitle=subtitle1,buttons=[button1,button2])
  
  bot.send_generic_message(sender,[element1])
```

<img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xfa1/t39.2365-6/13509243_818831098218750_489238139_n.png" alt="screenshot" width="500" height="450"> 


###Sending Quick Replies
#####create_quick_reply(title,payload)
you can attach them with text,photo,audio,videos

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  quick_reply1 = bot.create_quick_reply("Red","red")
  quick_reply2 = bot.create_quick_reply("Green","green")
  bot.send_message(sender,"Pick a color:",quick_reply=[quick_reply1,quick_reply2])
```

###Send Photos, Videos, Audios
####send_attachment(self, sender, type, url,metadata=None,quick_reply=None)

<img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xaf1/t39.2365-6/13466577_1753800631570799_2129488873_n.png" alt="screenshot" width="250" height="450"> 

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  bot.send_attachment(sender,"image",url="http://xyx.png")
  
  bot.send_attachment(sender,"video",url="http://xyx.mp4")
  
  bot.send_attachment(sender,"audio",url="http://xyx.mp3")
```

###Get User Info
####get_user(self,sender)

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  user = bot.get_user(sender)
```
Output :

```
{
  "first_name": "Peter",
  "last_name": "Chang",
  "profile_pic": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/p200x200/13055603_10105219398495383_8237637584159975445_n.jpg?oh=1d241d4b6d4dac50eaf9bb73288ea192&oe=57AF5C03&__gda__=1470213755_ab17c8c8e3a0a447fed3f272fa2179ce",
  "locale": "en_US",
  "timezone": -7,
  "gender": "male"
} 
```


##Thread Settings to improve user experience

You should visit [Thread Setting Page](https://developers.facebook.com/docs/messenger-platform/thread-settings)

you can enable this greetings, persistent menu, get started message using `curls` 

Note : Messenger Platoform is in beta, visiblity of different thread settings will took time.

###This is the first wrapper for messenger bot api. I tried to keep it really simple from understanding point of view. If you feel that you have something to contribute and imporve this wrapper, you are welcome to send pull requests. 

###I will mention every person's name who will contribute for it's developement.

####I hope you all will accept this initial start from me and start creating bots in python for messenger too.

