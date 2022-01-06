def twoSum(nums, target):
    answer =[]
    for i, num in enumerate(nums):
        if len(answer) == 2:
            break
        else:
            nums_use = nums[:]
            val = target - nums_use.pop(i)
            for new_num in nums_use:
                new_val = val - new_num
                if new_val == 0:
                    answer.append(nums.index(num))
                    if new_num == num:
                        nums.pop(nums.index(num))
                        answer.append(nums.index(new_num) + 1)
                    else:
                        answer.append(nums.index(new_num))
    return answer
