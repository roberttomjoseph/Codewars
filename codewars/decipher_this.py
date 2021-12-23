def decipher_this(string):
    
    wordlist = string.split()
    correct_list = []
    
    for word in wordlist:
        
        if word[-1].isdigit():
            correct_list.append(chr(int(word)))
            
        elif word[2].isdigit():
            letter1 = chr(int(word[0:3]))
            word_c1 = word.replace(word[0:3], letter1)
            lst = list(word_c1)
            lst1 = lst[:]
            lst1[-1] = lst[1]
            lst1[1] = lst[-1]
            word_corrected = ''.join(lst1)
            correct_list.append(word_corrected)
            
        else:
            letter1 = chr(int(word[0:2]))
            word_c1 = word.replace(word[0:2], letter1)
            lst = list(word_c1)
            lst1 = lst[:]
            lst1[-1] = lst[1]
            lst1[1] = lst[-1]
            word_corrected = ''.join(lst1)
            correct_list.append(word_corrected)
            
    return ' '.join(correct_list)


decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")