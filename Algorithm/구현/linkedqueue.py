class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next

    def popleft(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            answer = self.head.value
            self.head = None
            self.tail = None
            return answer

        answer = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return answer

    def show(self):
        s = '['
        curr = self.head
        while curr is not None:
            s += str(curr.value)
            curr = curr.next
        s += ']'
        print(s)

que = LinkedQueue()
que.append(3)
que.append(5)
que.append(7)
que.append(4)
que.append(7)
que.append(2)
que.append(7)
que.append(8)
que.append(7)
que.show()
print(que.popleft())
que.show()
print(que.popleft())
que.show()
print(que.popleft())
que.show()
print(que.popleft())
que.show()
print(que.popleft())
que.show()