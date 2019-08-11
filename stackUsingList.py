class Stack:
     def __init__(self):
         self.my_stack = []

     def isEmpty(self):
         return self.my_stack == []

     def push(self, item):
         self.my_stack.append(item)

     def pop(self):
         return self.my_stack.pop()

     def peek(self):
         return self.my_stack[len(self.my_stack)-1]

     def size(self):
         return len(self.my_stack)
         
s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
