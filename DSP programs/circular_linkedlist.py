class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self , value):
       new_node = Node(value)
       if not self.head:
          self.head = new_node
          new_node.next = self.head
       else:
          current = self.head
          while current.next != self.head:
            current = current.next
          current.next = new_node
          new_node.next = self.head
   
    def display(self):
       if not self.head:
          print("Circular Linked List is empty")
          return
       else:
          current = self.head
          while True:
             print(current.data)
             current = current.next
             if current == self.head:
                 break
 
cll = CircularLinkedList()

while True:
    print("1.Add value")
    print("2.Display value")
    print("3.Exit")
    
    choice = int(input("Enter the choice from above : "))
    
    if choice == 1:
        value = int(input("Enter the value to add : "))
        cll.append(value)
    elif choice == 2:
        cll.display()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid input")