def nth_triangle_num(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum


for i in range(384,10000):
    triangle_num = nth_triangle_num(i)
    factors = []
    for n in range(1,triangle_num+1):
        div = triangle_num/n
        if int(div) == div:
            factors.append(div)
    print(len(factors))
    if len(factors) > 500:
        print(i)
        break