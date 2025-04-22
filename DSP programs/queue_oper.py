class MyQueue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return self.queue == []
    
    def enqueue(self , value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("There was no one in the queue")
    
    def display(self):
        if not self.is_empty():
            for i in self.queue:
                print(i)
        else:
            print("There was no one in the queue")
    
queue1 = MyQueue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter the number from above : ")
    
    if choice == "1":
        value = input("Enter the value : ")
        queue1.enqueue(value)
    elif choice == "2":
        a = queue1.dequeue()
        if a is not None:
            print("Dequeue customer : ",a)
    elif choice == "3":
        queue1.display()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid input , input correctly")
    