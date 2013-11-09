'''
Tests for the has_free_food functions


Tests based on http://docs.python.org/2/library/unittest.html



Created on Nov 9, 2013

@author: Dabrowski
'''
import unittest
import sample_messages as samples

from utils.message.scanning import has_free_food as scanner

# Testing class
class TestRemoveTagsFunctions(unittest.TestCase):
    
    # Standard setup
 #   def setUp(self):
       # print "Message Processing Test Suite"

    # must not change an empty string        
    def test_empty_string(self):
        empty = ''
        self.assertEquals( scanner(empty), (False, "NO FOOD"))
            
    def test_definitely_has_food(self):
        hasFoodFOSHO = "FREE FOOD FOR ALL"
        ALSOHASFOOD = "I have pizza"
        foodPROVIDED = "Food will be provided"
        
        self.assertTrue(scanner(hasFoodFOSHO)[0])
        self.assertTrue(scanner(ALSOHASFOOD)[0])
        self.assertTrue(scanner(foodPROVIDED)[0])

    def test_real_messages_for_food(self):
        
        self.assertFalse(scanner(samples.BIG_STRING_1FINAL)[0])
        self.assertFalse(scanner(samples.BIG_STRING_2FINAL)[0])




if __name__ == '__main__':
    unittest.main()  