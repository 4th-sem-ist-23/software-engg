class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self , data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def update_node(self , old_data , new_data):
        temp = self.head
        while temp:
            if temp.data == old_data:
                temp.data = new_data
                return
            temp = temp.next
        print("Node was not found")
    
    def delete_at_end(self):
        if not self.head:
            print("Linked list is empty")
            return None
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def Display(self):
        temp = self.head
        while temp:
            print(temp.data , end="->")
            temp = temp.next
        print("None")
        
ll = LinkedList()

while True:
    print("1.Insert at end")
    print("2.Update the node")
    print("3.Delete at end")
    print("4.Display")
    print("5.Exit")
    
    choice = int(input("Enter the choice from above : "))
    
    if choice == 1:
        value = int(input("Value to add : "))
        ll.insert_at_end(value)
    elif choice == 2:
        old = int(input("Old value : "))
        new = int(input("New value : "))
        ll.update_node(old , new)
    elif choice == 3:
        ll.delete_at_end()
    elif choice == 4:
        ll.Display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Input Input!!!")