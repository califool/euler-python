# Problem 12
# What is the value of the first triangle number to have over five hundred divisors

from math import sqrt
divs = 500
tri_list = list()
n = 0
i = 0
tri_num = 0
while n < divs:
    i += 1
    tri_num += i
    tri_list = [1, tri_num]
    for j in range(2, round(sqrt(tri_num))):
        if tri_num % j == 0:
            tri_list.insert(1, j)
            if tri_num != j**2:
                tri_list.insert(1, tri_num // j)
    n = len(tri_list)
print("{}: {}".format(tri_num, tri_list[:]))
print("The amount of the divisors is {}".format(n))