def solution(coin, m):
    n = len(coin)
    dy = [0] * (m+1)
    dy[0] = 1 #1로 초기화로 해야 의도대로 코드가 구동된다.
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] += dy[j-coin[i]]
    return dy[m]


print(solution([2,3,5], 10))

def solution2(coin, m):
    dy = [1000] * (m+1)
    dy[0] = 0
    n = len(coin)
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] = min(dy[j], dy[j-coin[i]]+1)
    return dy[m]

print(solution2([1, 2, 5], 15))