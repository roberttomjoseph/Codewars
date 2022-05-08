# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

count = {1:0,89:0}

numbers = range(1,10000001)

def square_function(n):
    square_val = 0
    for digit in str(n):
        square_val += int(digit)**2
    return square_val

for number in numbers:
    square_sums = []
    square_sums.append(square_function(number))
    while square_function(square_sums[-1]) not in [1,89]:
        square_sums.append(square_function(square_sums[-1]))
    square_sums.append(square_function(square_sums[-1]))
    count[square_sums[-1]] += 1

print(count)

#Very, very inefficient and hacky implementation. Using memoization, and factorials and more advanced math in general can make this code much more efficient.