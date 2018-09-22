#In order to find the prime factors of a number, write the number as a product of prime numbers. 
#Then the distinct factors are the prime factors of the number: 
#35 is 5 times 7, 5 and 7 are prime, 
#So the prime factors of 35 are 5 and 7
#Write a function to find the largest prime factors

def prime_factor(n):

    i = 2
    while i * i < n:
         while n % i == 0:
             n = n / i
         i += i 
    return n
