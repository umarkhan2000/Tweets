'''A3. Tester for the function extract_mentions in tweets.
'''

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    '''Tester for the function extract_mentions in tweets.
    '''

    def test_empty(self):
        '''Empty tweet.'''

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        '''Non-empty tweet with no mentions.'''

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_nonempty_all_mention(self):
        '''Non-empty tweet with all mentions.'''
        
        arg = '@tweet @test @case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'test', 'case']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_nonempty_one_mention(self):
        '''Non-empty tweet with just one mention.'''
        
        arg = '@tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_nonempty_mention_nonvalid_mentions(self):
        '''Non-empty tweet with nonvalid mentions and regular mentions.'''
        
        arg = 'No valid @$ @mentions @! here?'
        actual = tweets.extract_mentions(arg)
        expected = ['mentions']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_nonempty_hashtag_and_mention(self):
        '''Non-empty tweet with hashtag and mentions as well as no mentions.'''
        
        arg = '@tweet #are @testable #and this is a @a @case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'testable', 'a', 'case']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_nonempty_mention_duplicate_captilized(self):
        '''Non-empty tweet with two of the same mention but one in caps'''
        
        arg = '@tweet @TWEET @test @TEST'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'tweet', 'test', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
    
  
    def test_nonempty_mention_containing_nonalphanumeric(self):
        '''Non-empty tweet with mentions that contain non-alphanumeric characters 
        and regular mentions.'''
        
        arg = '@many @cats$extra cats @meow?!'
        actual = tweets.extract_mentions(arg)
        expected = ['many', 'cats', 'meow']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        

   
    
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
