from solution import solution_first
from solution import solution_second

nums = [3, 3, 2, 2, 2, 4]
print(solution_first(nums))
nums = [3, 3, 3, 2, 2, 2]
print(solution_first(nums))
nums = [3, 3, 2, 2, 1, 4]
print(solution_first(nums))

a, b = 3, 5
print(solution_second(a, b))
a, b = 3, 3
print(solution_second(a, b))
a, b = 5, 3
print(solution_second(a, b))
