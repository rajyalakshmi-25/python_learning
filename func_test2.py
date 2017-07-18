'''
**Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

If you feel ambitious, explore the Collections module to solve this problem!
'''

def upper_lower(str):
    d = {"upcase":0, "lowercase":0}
    for char in str:
        if char.isupper():
            d["upcase"]+=1
        elif char.islower():
            d["lowercase"]+=1
        else:
            continue
    print "No of upper case charecters :",d["upcase"]
    print "No of Lower case Charecters :", d["lowercase"]
    pass
upper_lower("This is PYthon A Program")