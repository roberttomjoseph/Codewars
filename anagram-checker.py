def anagrams(word, words):
    anagram_list = []
    for element in words:
        for letter in element:
            if letter not in word:
                break
            elif element.count(letter) != word.count(letter):
                break
            elif element in anagram_list:
                break
            else:
                anagram_list.append(element)

    return anagram_list



print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))