#Write a function to count how many primes from 2 to input "n". List down the primes

def countprimes(n):
    b, p, ps = [True]*(n+1), 2, []
    for p in range (2, n+1):
        if b[p]:
            ps.append(p)
            for i in range(p, n+1, p):
                b[i] = False
    print (len(ps))
    return ps
