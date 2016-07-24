# -*- coding: utf-8 -*-

from messenger import messenger_api



class MessengerBot:

    #get_sender = ""
    
    def __init__(self, token):
        self.token = token

    def send_message(self, sender, text,metadata=None,quick_reply=None):

        return messenger_api.send_message(self.token,sender, text,metadata,quick_reply)
        
    def get_user(self,sender):
        return messenger_api.get_user(self.token,sender)
        
    def send_action(self, sender):

        return messenger_api.send_action(self.token,sender)

    def send_button_message(self, sender, text,buttons,metadata=None,quick_reply=None):
        return messenger_api.send_button_message(self.token, sender, text,buttons,metadata,quick_reply)
        
    def create_buttons(self, type,title,payload=None, url=None):     
        return messenger_api.create_buttons(type,title,payload,url)

        
    def create_elements(self, title,item_url=None,image=None,subtitle=None,buttons=[]):     
        return messenger_api.create_elements(title,item_url,image,subtitle,buttons)

        
    def send_generic(self, sender, elements,metadata=None,quick_reply=None):
        return messenger_api.send_generic(self.token,sender, elements,metadata,quick_reply)       

        
    def send_attachment(self, sender, type, url,metadata=None,quick_reply=None):
        return messenger_api.send_attachment(self.token,sender,type,url,metadata,quick_reply)
        
    def create_quick_reply(self,title,payload):
        return messenger_api.create_quick_reply(title,payload)
