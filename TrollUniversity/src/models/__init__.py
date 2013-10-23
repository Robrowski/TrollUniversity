from google.appengine.ext import db

class Message(db.Model):
    subject = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
#     files = db.ListProperty(db.LinkProperty,required=True)