# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_squares = 0
for n in range(1, 101):
    sum_squares += n**2

square_sum = 0
for n in range(1, 101):
    square_sum += n
square_sum = square_sum**2

print(square_sum - sum_squares)