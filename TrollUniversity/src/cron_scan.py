'''
Created on Oct 22, 2013

@author: Matt
'''
import webapp2
from models import Message
import utils
from datetime import datetime, timedelta
import calendar
import logging

class CronHandler(webapp2.RequestHandler):
    def get(self):
        beforeTime = datetime.now() - timedelta(minutes=30)
        afterTime = calendar.timegm(beforeTime.utctimetuple())
        uncheckedMessages = utils.getRecentMessages('trolluniversity.edu@gmail.com',afterTime)
#         for message in uncheckedMessages:
#             subject = message.subject
#             rawBody = message.get_body(type='text/html')
#             if rawBody:
#                 dbMessage = Message(subject = subject,
#                                     body = rawBody[0]['content'])
#                 dbMessage.put()