#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers
#is 9009 = 91 × 99.

# Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.

#loop through 2 digits and append to list
def multiples():
    multiplesNumbers = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            multiplesNumbers.append(i * j)
    return multiplesNumbers

# Check if string is palindrome
def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
        
# Loop through list and check for palindromes
palindrome = []
for i in multiples():
    if isPalindrome(i):
        palindrome.append(i)
    else: 
        pass
# print highest palindrome in list
print(max(palindrome))