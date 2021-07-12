import math

def solution(arr):
    n = len(arr)
    dy = [0] * n
    pa = [0] * n
    pa[0] = -1
    dy[0] = 1
    answer = 0
    idx = 0
    def DFS(idx):
        if idx == -1:
            return
        else: 
            DFS(pa[idx])
            print(arr[idx], end=' ')
    for i in range(1,n):
        max_val = 0
        pos = -1
        for j in range(i):
            if arr[j] < arr[i] and dy[j] > max_val:
                max_val = dy[j]
                pos = j
        dy[i] = max_val + 1
        pa[i] = pos
        # answer = max(answer, dy[i]) #answer 기존값보다 dy[i] 이 크면 answer이 해당 값이다.
        if dy[i]>answer:
            answer = dy[i]
            idx = i
    DFS(idx)
    print()
    return answer


print(solution([5,3,7,8,6,2,9,4]))