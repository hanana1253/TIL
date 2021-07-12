from collections import deque
import sys 
sys.stdin = open('anagram.txt', 'r')

a = input()
b = input()

sh = dict()
for x in a:
    sh[x] = sh.get(x, 0) + 1

for x in b:
    sh[x] = sh.get(x, 0) - 1

for x in a:
    if sh.get(x) > 0:
        print('NOOOOOOOO')
        break
else:
    print('ANAGRAM')