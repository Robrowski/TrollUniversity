'''
Created on Oct 14, 2013

@author: Matt
'''
import base_handler
from utils import gmail_retrieve as g

class FrontHandler(base_handler.Handler):
    def get(self):
        
        messages = g.getMessages()
        self.render("frontPage.html",
                    messages = messages)
