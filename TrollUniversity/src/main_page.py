from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from page_handlers import front_page

from models import Message

import json
import logging
from utils.message.processing import remove_tags as tagRemover

class WebhookHandler(webapp.RequestHandler):
    def post(self):
        message = json.loads(self.request.body)
        logging.error(message)
       
        subject = message['message_data']['subject']
        subject = tagRemover.remove_tags(subject)  # Remove the tags

        
        rawBody = message['message_data']['body'][0]['content']
        rawBody = tagRemover.remove_tags(rawBody)  # Remove the tags
        
        dbMessage = Message(subject = subject,
                            body = rawBody)
        
        #process
        # - normalize the email - 
        # removings tags
        
        
        # - check for duplicates
        
        dbMessage.put()
        
        #send notifications via txt etc.
        
        
        
        
        
application = webapp.WSGIApplication([('/', front_page.FrontHandler),
                                      ('/webhook',WebhookHandler)], 
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()