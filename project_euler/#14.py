def next_term(n):
    by_two = n/2
    if by_two == int(by_two):
        return by_two
    else:
        return 3*n + 1


max_length = 0
max_num = 0

for i in range(1,1000001):
    num = i
    length = 1
    while True:
        if i == 1:
            break
        i = next_term(i)
        length += 1
    if length > max_length:
        max_length = length
        max_num = num
        print(num,max_length)
        