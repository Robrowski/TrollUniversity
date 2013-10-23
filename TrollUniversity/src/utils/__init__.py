import settings
from _RequiredAPIs import contextio as c

context_io = c.ContextIO(consumer_key = settings.CONTEXTIO_OAUTH_KEY,
                         consumer_secret = settings.CONTEXTIO_OAUTH_SECRET)
 
def getRecentMessages(account,afterTime=None):
    accounts = context_io.get_accounts(email=account)
    if accounts:
        account = accounts[0]
        return account.get_messages(date_after=afterTime)
    
def extractFiles(rawBody):
    return 'files'