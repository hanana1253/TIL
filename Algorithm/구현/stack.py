class Stack:
    def __init__(self, capacity):
        self.top = 0
        self.capacity = capacity
        self.list = [None] * self.capacity
    
    def push(self, value):
        if self.top == self.capacity:
            return False
        else:
            self.list[self.top] = value
            self.top += 1
            return True
        
    def pop(self):
        if self.top == 0:
            return False
        else:
            self.top -= 1
            return self.list[self.top]

    def isEmpty(self):
        return self.top == 0

    def peek(self):
        return self.list[self.top -1]

st = Stack(10)
s = '352+*9-'
for char in s:
    if char.isdigit():
        st.push(int(char))
    else:
        rt = st.pop()
        lt = st.pop()
        if char == '+':
          st.push(lt+rt)
        elif char == '-':
          st.push(lt-rt)
        elif char == '*':
          st.push(lt*rt)
        elif char =='/':
          st.push(lt/rt)

print(st.peek())