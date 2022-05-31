import scipy.special

t = int(input())

test_conditions = []

for parent_iteration in range(t):
    test_condition = []
    line_two = input()
    n, q = int(line_two[0]), int(line_two[2])
    s = input()
    q_terms = []
    for k in range(q):
        q_terms.append(int(input()))
    test_condition.append(n)
    test_condition.append(s)
    test_condition.append(q_terms)
    test_conditions.append(test_condition)


for condition in test_conditions:
    n = condition[0]
    s = condition[1]

    useful_counts = []

    for ki in condition[2]:

        sub_strings = []

        for i in range(n):
            for l in range(i+1,n+1):
                sub_strings.append((s[i: l]))

        equal_dict = {}

        for sub in sub_strings:
            equal_dict[sub] = set()
            count = 0
            for match in sub_strings:
                if sub == match:
                    count += 1
                    equal_dict[sub].add(count)

        useful_substrings = [x for x in equal_dict if max(equal_dict[x]) >= ki]

        useful_count = 0
        for substr in useful_substrings:
            useful_count += (scipy.special.comb(max(equal_dict[substr]),ki) % (10**9 + 7))
        
        useful_counts.append(useful_count)
    
    for i in useful_counts:
        print(int(i))