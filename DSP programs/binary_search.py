def binary_search(elements , target):
    low , high = 0 , len(elements) - 1
    
    while low <= high:
        mid = (low+high)//2
        mid_element = elements[mid]
        
        if mid_element == target:
            return f"Value was found at index : {mid}"
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return "Value was not found in list"


# list elements should be sorted
list1 = [12 , 17 , 19 , 21 , 34 , 42]
print("List Values : ",list1)
tar = int(input("Enter the target element : "))
result = binary_search(list1 , tar)
print(result)



