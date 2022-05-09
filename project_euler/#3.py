# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

factors = []

for n in range(1,600851475143):
    if num % n == 0:
        factors.append(n)
        print(factors)

