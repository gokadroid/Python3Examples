class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next 

n1 = Node("Hello", None)  
n2 = Node("21", n1)
n3 = Node("Green", n2) 
n4 = Node("Blue", n3)
n5 = Node("Daniel", n4)  

# as the entry into our linked list
head = n5
fastPointer=head

while fastPointer != None:
  print(fastPointer.data)
  fastPointer=fastPointer.next
