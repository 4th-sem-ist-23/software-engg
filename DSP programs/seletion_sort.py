


def selection_sort(list1):
    length = len(list1)
    
    for i in range(length):
        min_value = i
        for j in range(i+1 , length):
            if list1[j] < list1[min_value]:
                min_value = j
        list1[i] , list1[min_value] = list1[min_value] , list1[i]
        
    
list1 = [89 , 43 , 32 , 12 , 10 , 34]
print("Unsorted list : ",list1)
selection_sort(list1)
print("Sorted list : ",list1)