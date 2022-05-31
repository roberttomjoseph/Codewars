num_testcases = int(input())
test_cases = []
for case in range(num_testcases):
    test_cases.append(input())

for s in test_cases:
    l = len(s)
    count = 0

    for index in range(1,l):
        if 2*s[:index] == s[:2*index]:
            l2 = int((l -2*index)/2)
            if s[2*index:] == 2*s[-1*l2:]:
                count +=1

    print(count)