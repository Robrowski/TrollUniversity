'''
Created on Oct 31, 2013

@author: Dabrowski
'''

# A method provided to remove html tags froma string
def remove_tags(string):
    newstring = remove_stuff_between(string, '<', '>')
    newstring = remove_stuff_between(newstring, '{', '}')
    newstring = remove_stuff_between(newstring, '[', ']')


    # remove extra spaces  
    while "  " in newstring:
        newstring = newstring.replace( "  ", " ");
    
    return newstring



def remove_stuff_between(string, tagS, tagF):
    start = string.find(tagS)
    modified = string
    
    while start != -1:
        end = modified.find(tagF, start)
        modified = modified[:start] + " " + modified[end + 1:]
        start = modified.find(tagS)

    return modified


