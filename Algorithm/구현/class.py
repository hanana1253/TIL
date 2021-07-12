from collections import deque
import sys 
sys.stdin = open('classinput.txt', 'r')
need = input()
n = int(input())
for i in range(n):
    plan = input()
    Q = deque(need) # for문 돌때마다 필수과목 목록이 새로 생성된다.
    for x in plan:
        if x in Q:
            if x != Q.popleft():
                print('#%d NO'%(i+1))
                break
    else:
        if len(Q) == 0:
            print('#%d YES'%(i+1))
        else:
            print('#%d NO'%(i+1))
print()

