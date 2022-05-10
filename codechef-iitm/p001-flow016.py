num = int(input())

case_list = []

for i in range(num):
    case = input().split(' ')
    int_case = [int(x) for x in case]
    case_list.append(int_case)

ans_case_list = []

for case in case_list:

    if case[0] > case[1]:
        lesser = case[1]
        greater = case[0]
    else:
        greater = case[1]
        lesser = case[0]
    
    while(lesser):
        greater, lesser = lesser, greater % lesser
    hcf = greater

    lcm = int(case[0] * case[1] / hcf)
    
    ans_case = [hcf, lcm]
    ans_case_list.append(ans_case)

for case in ans_case_list:
    print(case[0],case[1])
