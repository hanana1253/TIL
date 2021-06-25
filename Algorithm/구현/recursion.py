# def DFS(n):
#     if n == 0:
#         return
#     else:
#         DFS(n-1)
#         print(n)


# DFS(3)

def fibo(n):
    if dy[n] > 0:
        return dy[n]
    if n <= 2:
        return 1
    else:
        dy[n] = fibo(n-1) + fibo(n-2) 
        return dy[n]

dy = [0]*50
print(fibo(40))