'''
Tests for the remove_tags functions


Tests based on http://docs.python.org/2/library/unittest.html



Created on Oct 31, 2013

@author: Dabrowski
'''
import unittest
import sample_messages as samples

from utils.message.processing import remove_tags as tagRemover

# Testing class
class TestRemoveTagsFunctions(unittest.TestCase):
    
    # Standard setup
 #   def setUp(self):
       # print "Message Processing Test Suite"

    # must not change an empty string        
    def test_empty_string(self):
        empty = ''
        
        self.assertEquals(tagRemover.remove_tags(empty), empty)
    
    # must not change a string with no tags        
    def test_string_with_no_tags_1(self):
        noTags = 'pooop and poop and stuff '
        
        self.assertEquals(tagRemover.remove_tags(noTags), noTags)
    

    def test_1(self):
        toProcess = '<h1>Title</h1><p>This  is a<a href="http://www.udacity.com">link</a>.<p>'
        expected  = " Title This is a link . "
        
        self.assertEquals(tagRemover.remove_tags(toProcess), expected)

    def test_2(self):
        toProcess = "<hello>           <goodbye>"
        expected  = " "
        
        self.assertEquals(tagRemover.remove_tags(toProcess), expected)
        
    def test_3(self):
        toProcess = 'pooop  '
        expected  = "pooop "
        
        self.assertEquals(tagRemover.remove_tags(toProcess), expected)
 
    def test_big_real_message_1(self):
        toProcess = samples.BIG_STRING_1INIT
        
        expected  = samples.BIG_STRING_1FINAL
        self.assertEquals(tagRemover.remove_tags(toProcess), expected)
    
    def test_big_real_message_2(self):
        toProcess = samples.BIG_STRING_2INIT
        
        expected  = samples.BIG_STRING_2FINAL
        print "This is the next message that needs addressing..."
        print tagRemover.remove_tags(toProcess)
     #   self.assertEquals(tagRemover.remove_tags(toProcess), expected)
        
    
if __name__ == '__main__':
    unittest.main()  