'''
TEST DESCRIPTION

Testing Resource: http://docs.python.org/2/library/unittest.html

Created on )__________(, 2013

@author: Troll
'''
import unittest  # This is the main resource



# Example resource to test
# from utils.message.processing import remove_tags as tagRemover




# Testing class: This is the testing suite
class StupidTest(unittest.TestCase):
    
    # Standard setup: This is the "test fixtures" = setup
    def setUp(self):
        self.seq = range(10)

	# A test case
    # All tests must start with the letters "test" so that PyUnit notices them    
    def test_matt_is_dumb(self):
        empty = ''
        
        # call self."assertion statement"
        self.assertEquals(empty, empty)
        self.assertTrue(True, "weiner")

    

# Another thing that idk    
if __name__ == '__main__':
    unittest.main()