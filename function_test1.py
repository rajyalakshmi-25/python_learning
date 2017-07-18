#Functions and Methods Homework
#Complete the following questions:
#Write a function that computes the volume of a
# sphere given its radius.a

def vol(r):
    #V= 4/3*r^3*pie(3.14)
    v = (4/3) * (3.14) * (r**r)
    print v
    pass

vol(3)

#Write a function that
#checks whether a number is in a given range (Inclusive of high and low)
'''
def ran_check(num,low,high):
    if num in xrange(low,high+1) :
        print "numnerin range %s " %str(num)
    pass
'''
def ran_check(num,low,high):
    return num in xrange(low,high+1)

ran_check(3,2,10)

