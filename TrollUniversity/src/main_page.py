from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from page_handlers import front_page
import cron_scan




application = webapp.WSGIApplication([('/', front_page.FrontHandler),
                                      ('/rescan',cron_scan.CronHandler)], 
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()