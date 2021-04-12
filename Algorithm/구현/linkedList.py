class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def prepend(self, value):
        if self.head == None:
            new_node = Node(value, None)
        else:
            new_node = Node(value, self.head)
        self.head = new_node

    def append(self, value):
        if self.head == None:
            self.head = Node(value, None)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(value, None)

    def set_head(self, index):
        if self.head == None:
            print("No node exists")
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            self.head = curr

    def access(self, index):
        if self.head == None:
            print("No node exists")
        else: 
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr.value

    def insert(self, index, value):
        if self.head == None:
            print("No node exists")
        else:
            curr = self.head
            for _ in range(index):
                prev = curr
                curr = curr.next
            new_node = Node(value, curr)
            prev.next = new_node

    def remove(self, index):
        curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def print(self):
        pass

test = SinglyLinkedList()
print(test.is_empty())
print(test)
test.prepend(3)
print(test.is_empty())
print(test.access(0))
test.remove(0)
print(test.access(0))

