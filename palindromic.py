#A palindromic number reads the same both ways.
#Find the largest palindrome made from the product of two 3-digit numbers and what are the products

def palin(num):
    pal = str(num)
    return pal == pal[::-1]

result, ix, jx = 0, 0, 0    
for i in range(100, 1000):
    for j in range(i, 1000):
        if palin(i * j) and i*j > result:
            result = i * j
            ix, jx = i, j

print (result, ix, jx)
