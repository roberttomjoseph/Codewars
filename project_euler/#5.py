factor_dict = {}

prime_list = [2,3,5,7,11,13,17,19]
for j in prime_list:
    factor_dict[j] = 0


for i in range(1,21):
    factor_count = {}
    prime_list = [2,3,5,7,11,13,17,19]

    for j in prime_list:
        factor_count[j] = 0

    while len(prime_list) != 0:


        if int(i/prime_list[0]) == i/prime_list[0]:
            factor_count[prime_list[0]] += 1
            i = i/prime_list[0]

        if  int(i/prime_list[0]) != i/prime_list[0]:
            prime_list.remove(prime_list[0])
    
    for factor in factor_count:
        if factor_count[factor] > factor_dict[factor]:
            factor_dict[factor] = factor_count[factor]

answer = 1

for factor in factor_dict:
    answer = answer * factor * factor_dict[factor]

print(answer*3)