factorial = 1

for n in range(1,100):
    factorial = factorial * n

factorial_sum = 0

for n in str(factorial):
    factorial_sum += int(n)

print(factorial_sum)