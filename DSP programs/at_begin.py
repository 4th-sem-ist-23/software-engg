class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_at_beginning(self):
        if not self.head:
            print("Node are not present to delete")
            return
        self.head = self.head.next
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="->")
            temp = temp.next
        print("None")

ll = LinkedList()
while True:
    print("1.Insert at beginning")
    print("2.Delete at beginning")
    print("3.Display nodes")
    print("4.Exit")
    
    choice = int(input("Enter the choice from above : "))
    
    if choice == 1:
        value = int(input("Enter the value : "))
        ll.insert_at_beginning(value)
    elif choice == 2:
        ll.delete_at_beginning()
    elif choice == 3:
        ll.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid input !!!")
        
        