'''
Write a Python function to check whether a string is pangram or not.

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"

Hint: Look at the string module
'''
import string

x = string.ascii_lowercase
print x
a="abcdE"
a=a.lower()
print a

def pangram(str):
    str1 = str.lower()
    if( set(string.ascii_lowercase) <= set(str.lower())):
        print "ispangram"
        return True
    print "not pangram"

pangram('The quick brown fox jumps over the lazy dog')