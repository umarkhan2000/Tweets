'''A3. Tester for the function common_words in tweets.
'''

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    '''Tester for the function common_words in tweets.
    '''

    def test_empty(self):
        '''Empty dictionary.'''

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        '''Dictionary with one word.'''

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)

    def test_two_word_limit_one(self):
        '''Dictionary with two words which have different counts'''

        arg1 = {'hello': 2, 'bye': 1}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_two_word_repition_limit_one(self):
        '''Dictionary with two words which have same counts'''

        arg1 = {'hello': 3, 'bye': 3}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
    
    def test_six_word_limit_two(self):
        '''Dictionary with six words each having different counts'''

        arg1 = {'hello': 2, 'bye': 1, 'cats': 3, 'test': 4, 'case': 5, 'yes': 9}
        arg2 = 2
        exp_arg1 = {'case': 5, 'yes': 9}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
    
    def test_six_word_repitition_limit_three(self):
        '''Dictionary with six words each having different counts'''

        arg1 = {'hello': 4, 'bye': 3, 'cats': 2, 'test': 2, 'case': 2, 'yes': 2}
        arg2 = 3
        exp_arg1 = {'hello': 4, 'bye': 3}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)

    def test_many_words_mixed_value_limit_less_geq_greater(self):
        '''Dictionary with more than one word a few with same values and a
        few with unique values and limit is less than the keys in the dictionary
        and the limit is equal to the amount of words with the same values where
        the unique values and one key contains a maximum value'''
   
        arg1 = {'hello': 2, 'bye': 2, 'ok': 1, 'big': 3}
        arg2 = 2
        exp_arg1 = {'big': 3}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None
   
        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)
   
        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)                    
       
    def test_many_words_mixed_value_limit_geq(self):
        '''Dictionary with more than one word with a few unique values and 
        some same values with limits greater than or equal 
        to keys in the dictionary'''
       
        arg1 = {'hello': 2, 'bye': 1, 'hi': 1}
        arg2 = 3
        exp_arg1 = {'hello': 2, 'bye': 1, 'hi' : 1}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None
       
        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)
