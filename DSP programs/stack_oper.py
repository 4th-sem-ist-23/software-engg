class StackOper:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return self.stack == []
    
    def push(self , value):
        self.stack.append(value)
    
    def remove(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("Stack was empty")
    
    def display(self):
        if not self.is_empty():
            print("Stack elements : ")
            for i in self.stack:
                print(i)
        else:
            print("Stack was empty")
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack was empty")

stack1 = StackOper()

# optional code
'''
while True:
    print("1.Push")
    print("2.Remove")
    print("3.Display")
    print("4.Peek")
    print("5.Size")
    print("6.Exit")
    
    choice = int(input("Input from above option [1,2,3,4,5,6] : "))
    
    if choice == 1:
        value = int(input("Enter the value : "))
        stack1.push(value)
    elif choice == 2:
        stack1.remove()
    elif choice == 3:
        stack1.display()
    elif choice == 4:
        peek = stack1.peek()
        print(peek)
    elif choice == 5:
        size = stack1.size()
        print(size)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid Input!!")

'''
stack1.push(20)
stack1.push(10)
stack1.push(23)
stack1.display()
stack1.remove()
stack1.display()

print("Peek : ",stack1.peek())
print("Size : ",stack1.size())