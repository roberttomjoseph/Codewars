# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import math

palindrome_dict = {}
factor_list = [x for x in range(100,1000)]
factor_list2 = [x for x in range(100,1000)]


for i in factor_list:
    for j in factor_list2:
        product = i*j
    key = f'{i} x {j}'
    palindrome_dict[key] = product
    factor_list2.pop(0)
    print(palindrome_dict)

conf_palindromes = []

for key in palindrome_dict:
    potential_palindrome = str(palindrome_dict[key])
    conf_palindromes.append(potential_palindrome)
    for i in range(math.ceil(len(potential_palindrome)/2)):
        if potential_palindrome[i] != potential_palindrome[len(potential_palindrome)-1-i]:
            conf_palindromes.pop()
            break
        print(conf_palindromes)