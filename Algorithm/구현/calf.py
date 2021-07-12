from collections import deque

Max = 10000

ch = [0]*(Max+1)
dis = [0]*(Max+1)
s, e = map(int, input().split())

ch[s] = 1
dis[s] = 0

Q = deque()
Q.append(s)

while Q:
    now = Q.popleft()
    if now == e:
        break
    for next in (now-1, now+1, now+5):
        if ch[next] == 0:
            Q.append(next)
            ch[next] = 1
            dis[next] = dis[now] + 1

print(dis[e])