


def insertion_sort(elements):
    length = len(elements)
    
    if length <= 1:
        return
    for i in range(1 , length):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
            elements[j+1] = key
            

list1 = [23 , 1 , 12 , 45 , 19 , 71 , 62]
print("Unsorted list : ",list1)
insertion_sort(list1)
print("Sorted list : ",list1)

