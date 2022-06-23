# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

n = 2000000
primes = [2]

for i in range(3,1000):
    for j in primes:
        div = i/j
        if int(div) == div:
            pass
        else:
            primes.append(i)
            # if primes[-1] - primes[-2] > 1000:
    print(primes[-1])