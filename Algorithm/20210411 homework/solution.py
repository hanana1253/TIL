def solution_first(nums):
    if len(set(nums)) >= len(nums)/2:
        answer = int(len(nums)/2)
    else:
        answer = len(set(nums))
    return answer

from functools import reduce

def solution_second(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a    
    answer = reduce((lambda x, y : x + y), [i for i in range(a, b+1)])
    return answer