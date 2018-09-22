#Write a function to find the nth prime number.
Ex: 6th prime number is 13 (2,3,5,7,11,13)

def nth_prime_number(num):
    prime = [2]
    x = 3
    if num < 2:
        return 2
    while len(prime) < num:
        for y in prime:
            if x%y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2
    return prime[-1]
