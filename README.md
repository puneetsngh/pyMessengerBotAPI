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

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  
  bot.send_message(sender,"Hello Echo Bot")
```

###Using Buttons
####send_button_message(sender, text,buttons,metadata=None,quick_reply=None)
#####create_buttons(type,title,payload=None,url=None)
```
def process_message(data):              
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  text = data['entry'][0]['messaging'][0]['message']['text']
  
  button1 = bot.create_button("web_url","hello",url="http://google.com")
  button2 = bot.create_button("postback","test",payload="test123")
  
  bot.send_button_message(sender,"This is to test buttons",[button1,button2])
```

###Using Generic Messages
####send_generic(sender, elements,metadata=None,quick_reply=None):
#####create_element(title,item_url=None,image=None,subtitle=None,buttons=[])
```
def process_message(data):              
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  text = data['entry'][0]['messaging'][0]['message']['text']
  
  button1 = bot.create_button("web_url","hello",url="http://google.com")
  button2 = bot.create_button("postback","test",payload="test123")
  image1 = "http://xyz.png"
  subtitle1 = "testing generic messages"
  
  element1 = bot.create_element("Test1",image=image1,subtitle=subtitle1,buttons=[button1,button2])
  element1 = bot.create_element("Test1",image=image1,subtitle=subtitle1,buttons=[button1,button2])
  
  bot.send_generic_message(sender,[element1,element2])
```

###Sending Quick Replies
#####create_quick_reply(title,payload)
you can attach them with text,photo,audio,videos

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  quick_reply1 = bot.create_quick_reply("quick button","testing")
  bot.send_message(sender,"Hello Echo Bot",quick_reply=[quick_reply1])
```

###Send Photos, Videos, Audios
####send_attachment(self, sender, type, url,metadata=None,quick_reply=None)

```
def process_message(data):
  sender = data['entry'][0]['messaging'][0]['sender']['id']
  bot.send_attachment(sender,"image",url="http://xyx.png")
  
  bot.send_attachment(sender,"image",url="http://xyx.png")
  
  
```
