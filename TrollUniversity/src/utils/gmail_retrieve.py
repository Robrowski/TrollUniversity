'''
Created on Oct 13, 2013

@author: Matt
'''
import logging
import settings
from _RequiredAPIs import contextio as c

context_io = c.ContextIO(consumer_key = settings.CONTEXTIO_OAUTH_KEY,
                         consumer_secret = settings.CONTEXTIO_OAUTH_SECRET)
 
def getMessages():
    accounts = context_io.get_accounts(email='trolluniversity.edu@gmail.com')
    logging.debug(accounts)
    if accounts:
        account = accounts[0]
        print(account.get_messages())
        return account.get_messages()
