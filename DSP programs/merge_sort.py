

def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
  
		merge_sort(left)
		merge_sort(right)
  
		i = j = k = 0
  
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
   
list1 = [67 , 43 , 21 , 23 , 78 , 12]
print("Unsorted list : ",list1)
merge_sort(list1)
print("Sorted list : ",list1)