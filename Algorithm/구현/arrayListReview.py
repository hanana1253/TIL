import array

class ArrayList:
    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        return self.length == 0

    def prepend(self, value):
        self.insert(0, value)

    def append(self, value):
        self.insert(self.length, value)

    def set_head(self, index):
        self.array = self.array[index:]
        self.length -= index
        self.capacity -= index

    def access(self, index):
        if index > self.length:
            return False
        return self.array[index]

    def insert(self, index, value):
        if self.length == self.capacity:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(index):
                new_array[i] = self.array[i]
            for i in range(index, self.length):
                new_array[i+1] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, index - 1, -1):
                self.array[i+1] = self.array[i]
        self.array[index] = value
        self.length += 1

    def remove(self, index):
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        self.length -= 1

    def print(self):
        pass


test = ArrayList(5)
test.prepend(0)
test.prepend(1)
test.prepend(2)
test.prepend(3)
test.prepend(4)
print(test.array)