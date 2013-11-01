'''
Created on Oct 31, 2013

@author: Dabrowski
'''

# A method provided to remove html tags froma string
def remove_tags(string):
    start = string.find('<')
    newstring = string
    while start != -1:
        end = newstring.find('>', start)
        newstring = newstring[:start] + " " + newstring[end + 1:]
        start = newstring.find('<')
   
    # remove extra spaces  
    while "  " in newstring:
        newstring = newstring.replace( "  ", " ");
    
    return newstring





