from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from page_handlers import front_page




application = webapp.WSGIApplication([('/', front_page.FrontHandler)], 
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()