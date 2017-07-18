#Use range() to print all the even numbers from 0 to 10.

for l in range(0,11):
    if l%2 == 0:
        print  l
x = range(0,11,2)
print x

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
l = [ x for x in xrange(1,51) if x%3 == 0]
print l
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for wrd in st.split(" "):
    if len(wrd)%2 == 0:
       # print wrd+"-even number"


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


for num in xrange(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print num+"FizzBuzz"
    elif num % 5 == 0 :
        print "Buzz"
    elif num % 3 == 0 :
        print "Fizz"
    else:
        print num