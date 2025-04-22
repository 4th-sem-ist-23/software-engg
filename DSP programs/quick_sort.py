
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesspivot = [x for x in arr[1:] if x <= pivot]
        greaterpivot = [x for x in arr[1:] if x > pivot]
        
        return quicksort(lesspivot)+[pivot]+quicksort(greaterpivot)


arr = [90 , 56 , 42 , 14 , 78 , 9]
print("Unsorted list : ",arr)
result = quicksort(arr)
print("Sorted list : ",result)