def count_deaf_rats(town):
    rat_list = []

    for character in town:
        if character != ' ':
            if character != 'P':
                if len(rat_list) == 0:
                    rat_list.append(character)
                elif len(rat_list[-1]) == 1:
                    rat_list[-1] = rat_list[-1] + character
                elif len(rat_list[-1]) == 2:
                    rat_list.append(character)
            elif character == 'P':
                    rat_list.append('TP')

    if rat_list.index('TP') == 0:
        before_list = []
    else:
        before_list = rat_list[:rat_list.index('TP')]

    after_list = rat_list[rat_list.index('TP') + 1:]

    count = 0

    for rat in before_list:
        if rat == 'O~':
            count += 1
    for rat in after_list:
        print(rat)
        if rat == '~O':
            count += 1
    
    return count

count_deaf_rats("~O~O~O~OP~O~OO~")