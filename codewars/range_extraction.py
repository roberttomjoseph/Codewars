def solution(args):
    

    final_list = []
    temp_list = []
    for num in args:
        if len(temp_list) == 0:
            temp_list.append(num)
        elif num == temp_list[-1] + 1:
            temp_list.append(num)
        else:
            final_list.append(temp_list)
            temp_list = []
            temp_list.append(num)
            
    final_list.append(temp_list)
            
    ans_string = ''
            
    for range in final_list:
        if len(range) == 1:
            ans_string += str(range[0])
            ans_string += ','
        elif len(range) == 2:
            ans_string += str(range[0])
            ans_string += ','
            ans_string += str(range[1])
            ans_string += ','
        else:
            ans_string += str(range[0])
            ans_string += '-'
            ans_string += str(range[-1])
            ans_string += ','
            
    return ans_string[:-1]

            


solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])