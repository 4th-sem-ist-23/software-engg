class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self , value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete_at_beginning(self):
        if not self.head:
            print("Linked list is empty")
            return None
        self.head  = self.head.next
    
    def insert_at_index(self , index , value):
        if index == 0:
            self.insert_at_beginning(value)
            return
        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                print("Index out of range")
                return None
            temp = temp.next
        
        if temp is None:
            print("Index out of range")
            return None
        
        new_node.next = self.head
        self.head = new_node
        
    def delete_at_index(self , index):
        if index == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                print("Index out of range")
                return None
            temp = temp.next
        
        if temp is None or temp.next is None:
            print("Index out of range")
            return None
        
        temp.next = temp.next.next
        
  
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="->")
            temp = temp.next
        print("None")
        

ll = LinkedList()


while True:
    print("1.Insert at index")
    print("2.Delete at index")
    print("3.Display")
    print("4.Exit")
    
    choice = int(input("Enter the choice from above : "))
    
    if choice == 1:
        index = int(input("Index to add : "))
        value = int(input("Value to add : "))
        ll.insert_at_index(index , value)
    elif choice == 2:
        index = int(input("Index to delete : "))
        ll.delete_at_index(index)
    elif choice == 3:
        ll.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Input!!!")
    
    