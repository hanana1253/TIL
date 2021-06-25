class CircularQueue:
    def __init__(self, Qsize):
        self.front = 0
        self.rear = 0
        self.capacity = Qsize
        self.List = [None]*self.capacity

    def isEmpty(self):
        flag = False
        if self.front == self.rear and self.List[self.front] == None:
            flag = True
        return flag

    def isFull(self):
        flag = False
        if self.front == self.rear and self.List[self.front] != None:
            flag = True
        return flag

    def append(self, value):
        if not self.isFull():
            self.List[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True
        else:
            return False

    def popleft(self):
        if not self.isEmpty():
            answer = self.List[self.front]
            self.List[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return answer
        else:
            return None

    def show(self):
        out = []
        if self.isFull():
            out = self.List[self.front:] + self.List[:self.rear]
        elif not self.isEmpty():
            if self.front < self.rear:
                out = self.List[self.front:self.rear]
            else:
                out = self.List[self.front:] + self.List[:self.rear]
        return out

que = CircularQueue(5)
que.append(3)
que.append(5)
que.append(7)
que.append(7)
que.append(7)
print(que.show())
print(que.popleft())
print(que.show())