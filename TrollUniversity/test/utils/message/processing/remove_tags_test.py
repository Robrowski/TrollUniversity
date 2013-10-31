'''
Tests for the remove_tags functions


Tests based on http://docs.python.org/2/library/unittest.html



Created on Oct 31, 2013

@author: Dabrowski
'''
import random
import unittest
from utils.message.processing import remove_tags as tagRemover

# Testing class
class TestRemoveTagsFunctions(unittest.TestCase):
    
    # Standard setup
    def setUp(self):
        self.seq = range(10)

    # must not change an empty string        
    def test_empty_string(self):
        empty = ''
        
        self.assertEquals(tagRemover.remove_tags(empty), empty)
    
    # must not change a string with no tags        
    def test_string_with_no_tags_1(self):
        noTags = 'pooop and poop and stuff'
        
        self.assertEquals(tagRemover.remove_tags(noTags), noTags)
    
    
if __name__ == '__main__':
    unittest.main()