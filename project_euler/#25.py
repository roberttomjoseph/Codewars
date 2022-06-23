fib_nums = [1,1]

while len(str(fib_nums[-1])) < 1000:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])

print(len(fib_nums))