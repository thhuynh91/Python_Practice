#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers 
#and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers 
#and the square of the sum.

from functools import reduce
def sumx(nums1):
    total = 0
    for i in range(nums1 + 1):
        total += i**2
    return total

def sqr(nums2):
    total2 = 0
    total3 = 1
    for i in range(nums2 + 1):
        total2 += i
        total3 = total2**2
    return total3

print (sqr(100)-sumx(100))
