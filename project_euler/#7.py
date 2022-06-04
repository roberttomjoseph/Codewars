list_primes = [2]

for n in range(3,1000000):
    for i in list_primes:
        if n % i == 0:
            break
        elif list_primes[-1] == i:
            list_primes.append(n)
            print(list_primes[-1])
    if len(list_primes) == 10001:
        break