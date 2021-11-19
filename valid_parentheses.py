def valid_parentheses(string):
    
    if len(string) == 0:
        return True
    
    open_count = 0
    
    for character in string:
        if character == '(':
            open_count += 1
        elif character == ')':
            open_count -= 1
            if open_count < 0:
                return False
                break
            
    if open_count != 0:
        return False
    
    if open_count == 0:
        return True
     
valid_parentheses(")test")