l = [2,3,4,5,6]
for item in l:
    print item

'''
We've used for loops with lists,
how about with strings? Remember strings are a sequence so when we iterate through them we will be accessing each item in that string

'''
for letter in 'This is a string.':
    print letter

for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'Odd number'
'''
Tuples have a special quality when it comes to for loops. 
If you are iterating through a sequence that contains tuples,
 the item can actually be the tuple itself, 
 this is an example of tuple unpacking. 
 During the for loop we will be unpacking the tuple
  inside of a sequence and we can access the individual items inside that tuple!
'''

tl = [(2,3),(4,5)]

for t in tl:
    print t

for (t1,t2) in tl:
    print t2