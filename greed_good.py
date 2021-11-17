def score(dice):
    count = {}
    
    for die in dice:
        if die not in count:
            count[die] = 1
        else:
            count[die] += 1
            
    score = 0
    
    for die, count_of in count.items():
        
        if count_of == 1:
            if die == 1:
                score += 100
            elif die == 5:
                score += 50
        
        elif count_of == 2:
            if die == 1:
                score += 200
            elif die == 5:
                score += 100
        
        elif count_of == 3:
            if die == 1:
                score += 1000
            else:
                score += die*100
        
        elif count_of == 4:
            if die == 1:
                score += 1100
            elif die == 5:
                score += 550
            else:
                score = die * 100
                
        elif count_of == 5:
            if die == 1:
                score += 1200
            elif die == 5:
                score += 600
            else:
                score = die * 100
            
                
    return score
