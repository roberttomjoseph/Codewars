num = int(input())
case_list = [[int(x) for x in input().split(' ')] for i in range(num)]
for case in case_list:
    people = case[1]
    coins = case[0]
    max_rem = 0
    for i in range(1,people+1):
        if max_rem < coins % i:
            max_rem = coins % i
    print(max_rem)