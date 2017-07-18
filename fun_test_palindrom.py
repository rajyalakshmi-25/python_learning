'''
**Write a Python function that checks whether a passed string is palindrome or not.**

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run
'''

def palindrome(str):
    if str == str[::-1]:

        print "palindrome"
    pass

def is_palindrom(s):
    length = len(s)
    for i in range(length / 2):
        if s[i] != s[length - i - 1]:
            return False
    print "palindrom",s
    return True
is_palindrom("dada")
palindrome("happah")

