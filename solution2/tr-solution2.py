#Problem 2
#By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the *even-valued* terms.

def checkeven(n):
    if n % 2 == 0:
        return True
    else:
        return False

firstnumber = 1
secondnumber = 2
sum = 0
while firstnumber < 4000000:
    # Iterate through Fib sequence
    nextnumber = firstnumber + secondnumber
    firstnumber = secondnumber
    secondnumber = nextnumber
    # Check if even, if true, add to sum
    if checkeven(firstnumber):
        sum+=firstnumber
print(sum)