def first_non_repeating_letter(string):
    
    if len(string) == 0:
        return ''  
    
    if len(string) == 1:
        return string  
    
    string1 = string.lower()
    
    dict = {}
    
    for character in string1:
        if character in dict:
            dict[character] += 1
        if character not in dict:
            dict[character] = 1
            
    non_repeating_characters = []
    
    for character, count_of in dict.items():
        if count_of == 1:
            non_repeating_characters.append(character)
            
    if len(non_repeating_characters) == 0:
        return ''
            
    first_char = non_repeating_characters[0]
            
    if len(non_repeating_characters) == 1:
        first_char = non_repeating_characters[0]
    
    for character in non_repeating_characters:
        if string1.index(character) < string1.index(first_char):
            first_char = character
            
    return string[string1.index(first_char)]
        
    

first_non_repeating_letter('bbbbAcccdfg')