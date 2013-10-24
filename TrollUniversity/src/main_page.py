from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from page_handlers import front_page

from models import Message

import json
import logging
import cron_scan

class WebhookHandler(webapp.RequestHandler):
    def post(self):
        message = json.loads(self.request.body)
        logging.error(message['message_data']['body'][0]['content'])
        subject = message['message_data']['subject']
        rawBody = message['message_data']['body'][0]['content']
        dbMessage = Message(subject = subject,
                            body = rawBody)
        dbMessage.put()
        
application = webapp.WSGIApplication([('/', front_page.FrontHandler),
                                      ('/rescan',cron_scan.CronHandler),
                                      ('/webhook',WebhookHandler)], 
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()