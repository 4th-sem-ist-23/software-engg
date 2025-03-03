# Stack progarm using list and deque
# Stack follow the LIFO(Last-In First-Out) mean which elements is push last that elements is pop first
from collections import deque

# importing deque class using collections


'''
# performing Stack operation using list 

shop_site = []

shop_site.append("/home")
shop_site.append("/Eproducts")
shop_site.append("/earphones")
shop_site.append("/brand")
shop_site.append("/mi")

print(shop_site.pop())
print(shop_site.pop())
print(shop_site.pop())
print(shop_site.pop())
print(shop_site.pop())

list fails to act like stack : Because list is dynamic if the fixed lenght is filled. then list will create another one and copy from first and paste in other . 
create double amount of space than first part to store remaing elements.



'''

# performing stack operation using deque


stack = deque()

stack.append("/home")
stack.append("/Eproducts")
stack.append("/earphones")
stack.append("/brand")
stack.append("/mi")

print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

class Stack:
    def __init__(self):
        self.stack = deque()
    
    # display the elements
    def display(self):
        return self.stack
    
    # push the elements
    def push(self , value):
        self.stack.append(value)
    
    # pop the element from stack
    def pop(self):
        return self.stack.pop()
    
    # display the last mean peek element
    def peek(self):
        return self.stack[-1]
    
    # display the stack in boolean type if stack is empty then returns True or returns False
    def is_empty(self):
        return len(self.stack) == 0 
    
    # return size of the stack
    def size(self):
        return len(self.stack)
    

# creating the Stack class object
s1 = Stack()

# displaying the stack
print(s1.display())

# pushing elements to stack
s1.push(34)
s1.push(45)
s1.push(88)
s1.push(75)

# again displayint the stack
print(s1.display())

# pop(remove last element) removing the elements in stack
print(s1.pop())
print(s1.pop())

print(s1.display())

# displaying the peek(last element)
print(s1.peek())
print(s1.size())

print(s1.display())

# checking the status(stack is empty or not)
print(s1.is_empty())

print(s1.pop())
print(s1.pop())


print(s1.display())

print(s1.is_empty())
























