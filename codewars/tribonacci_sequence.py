def tribonacci(signature, n):
    sequence = signature

    if n < 4:
        if n == 0:
            return []
        else:
            return sequence[0:n]
        
    for _ in range(n-3):
        sequence += [sequence[-1] + sequence[-2] + sequence[-3]]
    return sequence

print(tribonacci([1,1,1],10))