import math
l = [5,5,5,5]

def distributive_sort(arr):
    s = sum(arr)
    m = min(arr)
    l = len(arr)
    res = [m + i for i in range(l)]
    
    index = l-1
    curr_sum = sum(res)
    
    if curr_sum == s:
        return res
    elif curr_sum > s:
        while curr_sum > s:
            res[(l-index-1)%l] -= 1
            curr_sum -= 1
            index -= 1
        return res
    else:
        while curr_sum < s:
            res[index%l] += 1
            curr_sum += 1
            index -= 1
        return res

            
        
        
    
