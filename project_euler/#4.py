# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import math

palindrome_dict = {}
factor_list = [x for x in range(100,1000)]
factor_list2 = [x for x in range(100,1000)]


for i in factor_list:
    for j in factor_list2:
        product = i*j
        key = f'{i}x{j}'
        palindrome_dict[key] = product
    print(len(palindrome_dict))
    factor_list2.remove(i)


conf_palindromes = []



for key in palindrome_dict:
    pot = str(palindrome_dict[key])
    conf_palindromes.append(pot)
    div = len(pot)/2
    if div == int(div):
        for i in range(div):
            if pot[i] != pot[(1+i)*-1]:
                conf_palindromes.remove(pot)
    print(conf_palindromes)
            