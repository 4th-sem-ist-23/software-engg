

def linear_search(list1 , target):
    for i in range(0 , len(list1) - 1):
        if list1[i] == target:
            return f"Target element index : {i}"
    else:
       return "Value was not found"


#elements can be unsorted
list1 = [10 , 20 , 30 , 40 , 50]
print("Elements of list : ",list1)
t_input = int(input("Enter the target element : "))

result = linear_search(list1 , t_input)
print(result)
