import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        return self.length == 0

    def prepend(self, value):
        for i in range(self.length):
          self.array[self.length-i] = self.array[self.length-(i+1)]
        #capacity가 충분할 경우 앞의 인덱스 값을 한개씩 뒤로 밀어주는 역 for문
        self.array[0] = value
        self.length += 1

    def append(self, value):
        #capacity가 충분할 경우 맨 뒤의 인덱스 값에 넣어주기.
        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        pass

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        for i in range(self.length - index):
          self.array[self.length-i] = self.array[self.length-(i+1)]
        array[index] = value
        self.length += 1
          
        pass

    def remove(self, index):
        for i in range(self.length-index):
            self.array[index+i] = self.array[index+i+1]
        self.length -= 1

    def print(self):
        pass
      
test = ArrayList(5)
test.prepend(3)
test.prepend(2)
test.prepend(1)
print(test.array)
test.append(4)
print(test.array)
print(test.access(2))
test.remove(2)
print(test.array)
print(test.access(2))