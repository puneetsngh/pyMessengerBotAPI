# -*- coding: utf-8 -*-
import requests
import json
import traceback
import sys
import cgi
import time
from datetime import *
from time import *
import os
import re
import urllib
import urllib2
import httplib

from sys import version_info
import string

reload(sys)
sys.setdefaultencoding('utf8')
import random
 
#text should be UTF-8 and has a 320 character limit

def send_message(token,sender,text,metadata,quick_reply):
    try:

        payload = {'recipient': {'id': sender}, 'message': {'text': text,'metadata':metadata,'quick_replies':quick_reply}}
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        print r

    except Exception as e:
        print e
        pass
        
        
def send_button_message(token,sender,text,buttons,metadata,quick_reply):
    try:
        payload =   {
                        "recipient": {
                            "id": sender
                        },
                        "message": {
                            "metadata":metadata,
                            "quick_replies":quick_reply,
                            "attachment": {
                                "type": "template",
                                "payload": {
                                    "template_type": "button",
                                    "text": text,
                                    "buttons": buttons
                                }
                            }
                        }
                    }
        print payload
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        print r
    except Exception as e:
        print e
        pass
    
#Number of buttons limited to 3 for a single message or a generic message per element

def create_buttons(type,title,payload=None,url=None):
    try:
        button_dic = {}
        button_dic["type"]=type
        button_dic["title"]=title
        button_dic["payload"]=payload
        button_dic["url"] = url
        return button_dic
    except Exception as e:
        print e
        pass

        
def send_action(token,sender):
    try:
        payload = {
                    "recipient": {
                        "id": sender
                    },
                    "sender_action": "typing_on"
                }

        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)

    except Exception as e:
        print e
        pass
        
        
def send_generic(token,sender,elements,metadata,quick_reply):
    try:
        payload = {
                    "recipient": {
                        "id": sender
                    },
                    "message": {
                        "metadata":metadata,
                        "quick_replies":quick_reply,
                        "attachment": {
                            "type": "template",
                            "payload": {
                                "template_type": "generic",
                                "elements": elements
                            }
                        }
                    }
                }    
        print payload
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        print r
            
    except Exception as e:
        print e
        pass
        

#type = "image", "audio", "video", "file"        
#url should be a single link
#iamge - jpg, png, gif
#audio type not specified but example shows mp3 supported
#video example also only show mp4

def send_attachment(token,sender,type,url,metadata,quick_reply): 
    try:
        payload = {
                    "recipient": {
                        "id": sender
                    },
                    "message": {
                        "metadata":metadata,
                        "quick_replies":quick_reply,
                        "attachment": {
                            "type": type,
                            "payload": {
                                "url": str(url)
                            }
                        }
                    }
                }    
                
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        print r
    except Exception as e:
        print e
        pass

#title has 80 character limit
#subtitle has 80 character limit
#buttons limited to 3
#image ratio is 1.91:1        
# elements array limit 10

def create_elements(title,item_url,image,subtitle,buttons): 

    try:
        elements_dict = {}
        elements_dict["title"] = title
        elements_dict["item_url"] = item_url
        elements_dict["image_url"] = image
        elements_dict["subtitle"] = subtitle
        elements_dict["buttons"] = buttons  

        return elements_dict
    except Exception as e:
        print e
        pass
        
        
#quick_reply has a limit of 10       
        
def create_quick_reply(title,payload): 
    try:
        reply_dict = {}
        reply_dict["content_type"]="text"
        reply_dict["title"] = title
        reply_dict["payload"] = payload
        return reply_dict
    except Exception as e:
        print e
        pass
        
        
def get_user(token,sender):
    try:
        r = requests.get('https://graph.facebook.com/v2.6/'+sender+'?access_token=' + token)
        return r.json()
    
    except Exception as e:
        print e
        pass
