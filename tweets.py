"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def alnum_prefix(text: str) -> str:
    """Return the alphanumeric prefix of text, converted to
    lowercase. That is, return all characters in text from the
    beginning until the first non-alphanumeric character or until the
    end of text, if text does not contain any non-alphanumeric
    characters.

    >>> alnum_prefix('')
    ''
    >>> alnum_prefix('IamIamIam')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!andMore')
    'iamiamiam'
    >>> alnum_prefix('$$$money')
    ''

    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'

    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []

    """
    final = []
    result = list(text.split())
    
    for word in result: 
        if word[0] == MENTION_SYMBOL:
            final.append(alnum_prefix(word[1:]))
            if alnum_prefix(word[1:]) == '':
                final.remove(alnum_prefix(word[1:]))
    return final    


def extract_hashtags(text: str) -> List[str]:
    """Return a list of all unique hashtags in text, converted to lowercase

    >>> extract_hashtags('Hi #UofT do you like #cats #CATS #meowmeow')
    ['uoft', 'cats', 'meowmeow']
    >>> extract_hashtags('#cats are #cute #cats #cat meow #meow')
    ['cats', 'cute', 'cat', 'meow']
    >>> extract_hashtags('#many #cats$extra #meow?!')
    ['many', 'cats', 'meow']
    >>> extract_hashtags('No valid #mentions #! here?')
    ['mentions']
    >>>extract_hashtags('No valid #! here?')
    []
    """
    final = []
    result = list(text.split())
    
   
    for word in result: 
        if word[0] == HASH_SYMBOL and alnum_prefix(word[1:]) not in final:
            final.append(alnum_prefix(word[1:]))
            if alnum_prefix(word[1:]) == '':
                final.remove(alnum_prefix(word[1:]))
    return final

def count_words(text: str, amount_of_words: Dict[str, int]) -> None:
    """
    >>>count_words('Hello whats my #name name', {})
    >>>result = {'hello': 1, 'whats': 1, 'my': 1, 'name': 1}
    >>>result == count_words('Hello whats my #name name', {})
    
    """
    
    lst = text.split(' ')
    
    for word in lst:
        if check_for_symbols(word) and clean_word(word) not in \
           amount_of_words and not word == '':
            amount_of_words[clean_word(word)] = 1
        elif check_for_symbols(word) and clean_word(word) in \
             amount_of_words and not word == '':
            amount_of_words[clean_word(word)] += 1

def common_words(words: Dict[str, int], count: int) -> None:
    """
    modify words so it contains N words with the highest frequency
    if there are words with the same frequency and by adding those words will
    exceed N, then omit them from the dictionary other wise keep them
    """
    
    original_order = list(words.values())
    max_to_min = list(reversed(sorted(words.values())))
    temp_lst1 = []
    temp_lst2 = []
    
    
    if count == len(words):
        words = words
        
    
    for num in range(len(max_to_min)):
        if len(temp_lst1) < count:
            temp_lst1.append(max_to_min[num])
    
    for nums in range(len(temp_lst1)):
        max_to_min.remove(temp_lst1[nums])
        
               
    temp_lst2 = remove_repeats(max_to_min, temp_lst1)
            
    a = reformat_order(original_order, temp_lst2)
    
    words_to_counts = combine_list(format_dict(words, a), a)
    
    words.clear()
    
    for keys in words_to_counts:
        words[keys] = words_to_counts[keys]
   

def read_tweets(filename: TextIO) -> Dict[str, List[tuple]]: 
    """ This function reads a text file and puts the information into a 
    dictionary, where the keys are the twitter usernames, and the values
    are a list of tuples(like tweet date, source, tweet count etc..) 
    """
    
    #file_tweet = open(filename, 'r')
    
    tweet_dict = {} 
    list_tuple = []
    tuple_tweet = ()
    text_tweet = ''
    
    for lines in filename.readline(): 
        line = lines.strip()
        if '<<<EOT' not in line:
            if line != '\n' and line.endswith(':'):
                username = line[0:line.find(':')].lower()
            elif line[0:14].isnumeric(): 
                source = line.split(',')
                date = int(source[FILE_DATE_INDEX])
                source = source[FILE_SOURCE_INDEX]
                favourite_count = int(source[FILE_FAVOURITE_INDEX])
                retweet = int(source[FILE_RETWEET_INDEX])
            else: 
                text_tweet += line 
        else:
            tuple_tweet = (text_tweet, date, source,
                           favourite_count, retweet)
            list_tuple = list_tuple + [tuple_tweet]
            tweet_dict[username] = list_tuple
            text_tweet = ''
            
    return tweet_dict


def hashtag_seperator(s: List[tuple]) -> List[str]:
    """Returns a list of the hashtags in s
    >>>hashtag_seperator([('hey wad is #up ajdnk', 2018, 'twitter', 39, 189),\
    ('ok #slau  sndgkndjnjsen', 2020, 'twitter', 14, 78)])
    ['up' , 'slau']
    """
    result = []
    for tups in s:
        text = tups[0]
        result = result + extract_hashtags(text)
    return result    

def detect_author(user_to_tweets: Dict[str, List[tuple]], tweet_text: str) -> \
    str:
    """Returns the username of the author who is most likely the
    author of the tweet based on the hashtags they use. If all 
    hashtags are uniquely used then return the username otherwise 
    return 'unknown'
    """
    acc = []
    
    for keys in user_to_tweets:
        author_hashes = hashtag_seperator(user_to_tweets[keys])
        text_hashes = extract_hashtags(tweet_text)
        if set(text_hashes).issubset(author_hashes):
            acc.append(keys)
    if len(acc) == 1:
        return acc[0]
    return 'unknown'

def most_popular(user_to_tweet: Dict[str, List[tuple]], date1: int, date2: int)\
    -> str:
    """Returns the username who was most popular on Twitter between
    the two dates. If tie or no tweets in date range, return 'Tie'
    
    >>> user_to_tweet = {'funkyt': [('hey', 2018, 'twitter', 39, 189),\
    ('bye', 2019, 'twitter', 54, 932), ('ok', 2020, 'twitter', 14, 78)], 
    'jaffal': [('no', 2018, 'twitter', 152, 76),
    ('yo', 2019, 'twitter', 102, 56), ('rich', 2020, 'twitter', 124, 3483)]}
    >>> most_popular(user_to_tweet, 2018, 2018)
    'tie'
    >>> most_popular(user_to_tweet, 2018, 2019)
    'funkyt'
  
    """
    user_to_pop = {}
    most_popular_user = ''
    count = 0
    
    
    for user in user_to_tweet:
        popularity = 0
        for i in range(len(user_to_tweet[user])):
            if user_to_tweet[user][i][TWEET_DATE_INDEX] >= date1 and\
               user_to_tweet[user][i][TWEET_DATE_INDEX] <= date2:
                popularity = popularity + \
                    user_to_tweet[user][i][TWEET_FAVOURITE_INDEX] +\
                    user_to_tweet[user][i][TWEET_RETWEET_INDEX]
        user_to_pop[user] = popularity
        
    for users in user_to_pop:
        if user_to_pop[users] == \
           max(user_to_pop.values()):
            most_popular_user = most_popular_user + users
            count = count + 1
            
    if count > 1:
        return 'tie'
    return most_popular_user


def combine_list(lst1: List[str], lst2: List[int]) -> Dict[str, int]:
    """Returns a dictionary with the keys being the items of lst1 and the values
    being the items of lst2
    
    precondition: len(lst1) == len(lst2) and len(lst1) and len(lst2) > 0
    >>>combine_list(['a','b','c'],[1,2,3])
    {'a': 1,'b': 2, 'c': 3}    
    """
    final = {}
    i = 0
    
    for item in lst1:
        final[item] = lst2[i]
        i = i + 1
    
    return final

def remove_repeats(list1: List[int], list2: List[int]) -> List[int]:
    """Returns a new list which removes the numbers that repeat from list2 in 
    list1
    >>>remove_repeats([1,2,4],[4,5,6])
    [5, 6]
    >>>remove_repeats([22,23,33],[22,45,33,42])
    [45, 42]
    >>>remove_repeats([7,8,9],[9,8,7])
    []
    """
    result = []
    for num in list2:
        if num not in list1:
            result.append(num)
            
    return result

def reformat_order(list1: List[int], list2: List[int]) -> List[int]:
    """Returns a modified list1 so that it gets rid of all the numbers which are
    not included in list2. List2 is in descending order.
    >>>reformat_order([1,2,4,5,3],[5,4,2])
    [2, 4, 5]    
    >>>reformat_order([100,23,44,33,45],[100,45,44])
    [100, 44, 45]
    """
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
            
    return result

def format_dict(words_dict: Dict[str, int], format_lst: List[int]) -> List[str]:
    """Returns a list of the keys of the dictionary words_dict that have the 
    corresponding values in format_list
    >>>format_dict({'a' : 1, 'b' : 3, 'c' : 4, 'd' : 3, 'e':4 , 'f':2}, [4, 4])
    ['c', 'e']
    >>>format_dict({'a' : 1, 'b' : 3, 'c' : 4, 'd' : 3, 'e':4 , 'f':4}, [3, 4, 3, 4])
    ['b', 'c', 'd', 'e']
    """
    key_lst = list(words_dict.keys())
    
    for keys in words_dict:
        if words_dict[keys] not in format_lst:
            key_lst.remove(keys)
            
    return key_lst

def check_for_symbols(word: str) -> bool:
    """Returns False if HASH_SYMBOL or MENTION_SYMBOL or URL_START are the
    beginning of a word
    
    >>>check_for_symbols('@helo')
    False
    >>>check_for_symbols('#helo')
    False
    >>>check_for_symbols('bob')
    True
    """
    
    if MENTION_SYMBOL in word or HASH_SYMBOL in word or URL_START in word:
            return False
    return True 

            

if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
