# -*- coding: utf-8 -*-
import requests
import json
import traceback
import sys

import logging
from sys import version_info
import string
reload(sys)
sys.setdefaultencoding('utf8')


import messenger

from flask import Flask, request


app = Flask(__name__)

token = "#Enter Your Token Here"

bot = messenger.MessengerBot(token)
print bot

@app.route('/', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:

        data = json.loads(request.data)
        print data
        for key in data['entry'][0]['messaging'][0].keys():

			#This manages all kinds of data recieved by the bot as per the features you enable in webhook on facebook developer portal
		
            if key =='message':
                if "is_echo" in data['entry'][0]['messaging'][0]['message']:
                    pass
                elif "attachments" in data['entry'][0]['messaging'][0]['message']:
                    
                    if data['entry'][0]['messaging'][0]['message']["attachments"][0]["type"]=="image":
                        process_photo(data)
                        pass
                    elif data['entry'][0]['messaging'][0]['message']["attachments"][0]["type"]=="video":
                        process_video(data)
                        pass
                    elif data['entry'][0]['messaging'][0]['message']["attachments"][0]["type"]=="audio":
                        process_audio(data)
                        pass
                    elif data['entry'][0]['messaging'][0]['message']["attachments"][0]["type"]=="file":
                        process_file(data)
                        pass
                    elif data['entry'][0]['messaging'][0]['message']["attachments"][0]["type"]=="location":
                        process_location(data) 
                        pass
                else:
                    process_message(data)   #process your text messages
                    pass
            elif key=="postback":
                print "in here"
                process_postback(data)
            elif key =="delivery":
                print data
                print "Here You can right the logic for what the bot should do when you recieve the delivery confirmation"
                
            elif key =="read":
                print data
                print "Here You can right the logic for response when the user reads the message"
            else:
                pass

    except Exception as e:
      print (traceback.format_exc()) # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == '9650769697':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token for Bot"
  return "Hello World" 

# For simple working you should only deal with this part for your bot  
  
def process_message(data):
    try:
        text = data['entry'][0]['messaging'][0]['message']['text'] 
        sender = data['entry'][0]['messaging'][0]['sender']['id'] 

            bot.send_message(sender,"This is a sample text")
    except Exception as e:
        print e
        pass


        
def process_postback(data):

    payload = data['entry'][0]['messaging'][0]['postback']['payload']
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    bot.send_action(sender)
    
    quick_reply1 = bot.create_quick_reply("Hi,"hello")
    bot.send_message(sender, payload,quick_reply=[quick_reply1])
    

def process_photo(data):

    try:
        sender = data['entry'][0]['messaging'][0]['sender']['id'] 

        bot.send_message(sender,"You sent an photo.")

    except Exception as e:
        print 'excepttion in pm1'+str(e)
        pass

def process_video(data):
    sender = data['entry'][0]['messaging'][0]['sender']['id'] 

    bot.send_message(sender,"You sent an video")
        
        
def process_audio(data):
    sender = data['entry'][0]['messaging'][0]['sender']['id'] 
    quick_reply1 = bot.create_quick_reply("send yes","yes")
    bot.send_message(sender,"You sent an audio",quick_reply=[quick_reply1])

def process_file(data):
    sender = data['entry'][0]['messaging'][0]['sender']['id'] 

    bot.send_message(sender,"You sent a file.")

def process_location(data):
    sender = data['entry'][0]['messaging'][0]['sender']['id'] 

    bot.send_message(sender,"You sent a location.")
    
    
if __name__ == '__main__':
    app.run(port=8001,debug=True)
