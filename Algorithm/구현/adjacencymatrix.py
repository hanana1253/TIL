from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


def DFS(v):
    global cnt
    if v == n:
        for x in path:
            print(x, end=' ')
        cnt += 1
        print()

    else:
        for i in range(1, n+1):
            if ch[i] == 0 and graph[v][i]==1:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

cnt = 0
ch[1] = 1
path = list()
path.append(1) #경로 추가하기 위해서 넣어준다.
DFS(1)
print()
print(cnt)