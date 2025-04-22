

class CircularQueue:
    def __init__(self , capacity):
        self.capacity = capacity
        self.items = [None]*capacity
        self.front = self.rear = -1
    
    def is_empty(self):
        return self.rear == self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self , value):
        if self.is_full():
            print("Circular Queue is full can't add value")
            return None
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] =  value
            print("Value added sucessfully")
    
    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is empty can't remove value")
            return None
        else:
            removed_value = self.items[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            
            return removed_value
    
    def display(self):
        if self.is_empty():
            print("Circular Queue is empty can't dispaly values")
            return None
        else:
            i = self.front
            print("Elements are : ")
            while True:
                print(self.items[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.capacity

cq_len = int(input("Enter the length of the circular queue : "))
cq1 = CircularQueue(cq_len)
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    
    choice = int(input("Enter the choice from above : "))
    
    if choice == 1:
        value = int(input("Enter the value to add : "))
        cq1.enqueue(value)
    elif choice == 2:
        removed_value = cq1.dequeue()
        if removed_value is not None:
            print("Dequeue Element : ",removed_value)
    elif choice == 3:
        cq1.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Input")
    
    


        