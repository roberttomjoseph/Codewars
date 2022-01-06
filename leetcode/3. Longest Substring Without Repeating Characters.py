def lengthOfLongestSubstring(s):
    
    count_list = []
    count = 0 
    substring = ''
    
    for letter in s:
        if count != 0:
            if letter in substring:
                count_list.append([count])
                count = 0
                substring = ''
        count += 1
        substring += letter
        
    count_list.sort()
    return count_list[-1]
        
            
            
            
lengthOfLongestSubstring('pwwkew') 