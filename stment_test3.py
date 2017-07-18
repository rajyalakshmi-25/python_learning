for num in xrange(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print "FizzBuzz"+str(num)
    elif num % 5 == 0 :
        print "Buzz"
    elif num % 3 == 0 :
        print "Fizz"
    else:
        print num


#Use List Comprehension to
# create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
str1 = [word[0] for word in st.split(" ")]
print str1