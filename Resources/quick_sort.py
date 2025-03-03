import shutil
import time


# Quick sort follows these steps 
# check the base condition that if arr contains 1 elements then it is sorted
# choose the pivot element
# place smaller values then pivot in left 
# place greater values then pivot in right
# perform these steps recursively to both left and right
# combine the sorted values and make the list or array sorted

usage = shutil.disk_usage(path=r"C:\Users\Hp\Documents")
s_time = time.time()


def quick_sort(elements):
    if len(elements) <= 1:
        return elements
    
    pivot = elements[0]
    left = [x for x in elements[1:] if x < pivot]
    right = [x for x in elements[1:] if x >= pivot]
    
    
    return quick_sort(left) + [pivot] + quick_sort(right)
    


elements = [45,67,32,13,89,2,13]
print(quick_sort(elements))
e_time = time.time()


print("Disk usage statistics : ", usage)
print("Time Complexity of the progarm : ",e_time - s_time);
