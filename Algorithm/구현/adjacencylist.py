import sys
sys.stdin = open('input.txt', 'r')

def DFS(v):
    global cnt
    if v == n:
        for x in path:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for next in graph[v]:
            if ch[next] == 0:
              ch[next] = 1
              path.append(next)
              DFS(next)
              ch[next] = 0
              path.pop()


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

cnt = 0
ch[1] = 1
path = list()
path.append(1) #경로 추가하기 위해서 넣어준다.
DFS(1)
print()
print(cnt)