

def bubble_sort(elements):
    length = len(elements)
    
    
    for i in range(length - 1):
        swapped = False
        for j in range(0 , length - i - 1):
            if elements[j] > elements[j+1]:
                swapped = True
                elements[j] , elements[j+1] = elements[j+1] , elements[j]
        if not swapped:
            return

list1 = [8 , 32 , 45 , 21 , 2 , 12 , 1 , 13]
print("Unsorted list : ",list1)
bubble_sort(list1)
print("Sored list : " , list1)