def fib_numbers_memoized(n):
    memo = []
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_numbers_memoized(n-1) + fib_numbers_memoized(n-2)
        return memo[n]

print(fib_numbers_memoized(111))