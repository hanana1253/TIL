n = 15

def solution(num):
    length = num//2 + 1
    arr = [i+1 for i in range(length)]
    sum = 0
    lt = 0
    answer = 0
    for rt in range(length):
        sum += arr[rt] 
        if sum == num:
            answer += 1
        while sum >= num:
            sum -= arr[lt]
            lt += 1
            if sum == num:
                answer += 1
    return answer

print(solution(n))