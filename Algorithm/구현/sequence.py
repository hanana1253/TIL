n = 8
m = 6
sequence = [1, 2, 1, 3, 1, 1, 1, 2]

# for문 중첩으로 하는 경우

count = 0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += sequence[j]
        if sum == m:
            count += 1
            break
        elif sum > m :
            break

print(count)

# sliding-window와 two-pointers의 combination
def solution(arr, m):
    lt = 0
    sum = 0
    answer = 0
    n = len(arr)
    for rt in range(n):
        sum += arr[rt]
        if sum == m:
            answer += 1
        while sum >= m:
            sum -= arr[lt]
            lt += 1
            if sum == m:
                answer += 1
    return answer

print(solution(sequence, m))
            