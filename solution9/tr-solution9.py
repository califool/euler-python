# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        for c in range(b, 1000 - b):
            if a + b + c == 1000:
                if is_pythagorean_triplet(a, b, c):
                    print(a, b, c)
                    print("Product: ", int(a * b * c))
                    exit(0)
