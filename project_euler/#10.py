# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


prime_list = [2]
for n in range(3,2000001):
    for i in prime_list:
        if n % i == 0 or i > n**2:
            break
        elif prime_list[-1] == i:
            prime_list.append(n)
            print(prime_list[-1])
                

print(prime_list)