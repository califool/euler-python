#Problem 3
#What is the largest prime factor of the number 600851475143?
def primefactor(n):
    p = 2
    while n >= p * p:
        if n % p == 0:
            n = n / p
        else:
            p = p + 1
    print(int(n))

primefactor(600851475143)