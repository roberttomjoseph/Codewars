def encode(st):
    list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    corresp_num = ['1', '2', '3', '4', '5']
    for letter in st:
        list.append(letter)
        if list[-1] in vowels:
            list[-1] = corresp_num[vowels.index(list[-1])]
    new_string = ''
    for element in list:
        new_string = new_string + element
    return new_string


def decode(st):
    list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    corresp_num = ['1', '2', '3', '4', '5']
    for letter in st:
        if letter in corresp_num:
            list.append(vowels[corresp_num.index(letter)])
        else:
            list.append(letter)
    new_string = ''
    for element in list:
        new_string = new_string + element
    return new_string

    