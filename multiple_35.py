#Find the sum of all the multiples of 3 or 5 below 1000.

def mul35(nums):
    total = 0
    for i in range(0, nums):
        if i%3 == 0 or i%5 == 0:
            total += i
    return total

#in short
#sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])
