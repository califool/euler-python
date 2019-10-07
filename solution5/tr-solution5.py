# Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers 
# from 1 to 20?
count = 2520
check = [11, 13, 14, 16, 17, 18, 19, 20]
while True:
    if all(count % i == 0 for i in check):
        break
    count += 2520
print(count)