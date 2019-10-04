#Problem 6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOfSquares = 0
squareOfSum = 0
for i in range(1,101):
    sumOfSquares += i * i
    squareOfSum += i 

squareOfSum= squareOfSum * squareOfSum
print("sum of Squares: ", sumOfSquares)
print("Difference : ",   squareOfSum - sumOfSquares)