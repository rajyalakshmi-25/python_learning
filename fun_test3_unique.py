'''
____
**Write a Python function that takes a list and returns a new list with unique elements of the first list.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
'''
def unique(l):
    d = []
    for num in l :
        if num not in d:
             d.append(num)
        else :
            continue
    return d
'''
 keys = {}
   for e in l:
       keys[e] = 1
   return keys.keys()

by using set
set makes the unique list of
how to declare set is set = {}
'''
import sets

def uniquie_sets(list):
    return set(list)


m = unique([1,2,3,4,5,6,1,2,3,3,3,4,4,5,5])
print m

s = uniquie_sets([2,3,4,5,5,5,3,3,3,3,1,1,2])
print s
print list(s)

'''
**Write a Python function to multiply all the numbers in a list
'''
def multi(li):
    mul = 1
    for num in li:
        mul*=num
    print mul
    return mul

multi([2,3,5,-1])