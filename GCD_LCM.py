#Write a function to find out what is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


from functools import reduce
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

print(reduce(lcm, range(1, 20+1)))
