import array
from collections import deque

class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)

    def preorder(self):
        def DFS(idx):
            if idx >= len(self.array):
                return
            else:
                print(self.array[idx])
                DFS(idx * 2 + 1)
                DFS(idx * 2 + 2)
        DFS(0)

    def inorder(self):
        def DFS(idx):
            if idx >= len(self.array):
                return
            else:
                DFS(idx * 2 + 1)
                print(self.array[idx])
                DFS(idx * 2 + 2)
        DFS(0)

    def postorder(self):
        def DFS(idx):
            if idx >= len(self.array):
                return
            else:
                DFS(idx * 2 + 1)
                DFS(idx * 2 + 2)
                print(self.array[idx])
        DFS(0)

bt = BinaryTree([0, 1, 2, 3, 4, 5, 6])
bt.preorder()
print('----------------')
bt.inorder()
print('----------------')
bt.postorder()