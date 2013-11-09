'''
Created on Nov 9, 2013

@author: Dabrowski
'''


highProbsKeywords = ['food', 'beverage']
lowProbKeywords   = ['free', 'provided', 'pizza']




def has_free_food(message):
    message = message.lower()
    
    for keys in highProbsKeywords:
        if keys in message:
            return True, "There's a good chance here"
    
    for keys in lowProbKeywords:
        if keys in message:
            return True, "There's a decent chance here"

    return False, "NO FOOD"