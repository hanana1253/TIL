from collections import deque

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def DFS(root):
            if root is None:
                return
            else:
                print(root.value)
                DFS(root.left)
                DFS(root.right)
        DFS(self.root)
        print()
    
    def inorder(self):
        def DFS(root):
            if root is None:
                return
            else:
                DFS(root.left)
                print(root.value)
                DFS(root.right)
        DFS(self.root)
        print()
    
    def postorder(self):
        def DFS(root):
            if root is None:
                return
            else:
                DFS(root.left)
                DFS(root.right)
                print(root.value)
        DFS(self.root)
        print()

    def bfs(self):
        Q = deque()
        Q.append(self.root)
        while Q:
            cur = Q.popleft()
            print(cur.value)
            if cur.left != None:
                Q.append(cur.left)
            if cur.right != None:
                Q.append(cur.right)

    def dfs(self, value):
        return False

tree = BinaryTree([i for i in range(7)])
tree.preorder()
tree.inorder()
tree.postorder()
tree.bfs()