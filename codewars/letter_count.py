def letter_count(s):
    dict = {}
    for letter in s:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

letter_count('arithmetic')