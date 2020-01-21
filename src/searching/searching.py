# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
    middle = (low+high)//2
    if target < arr[middle]:
      high = middle-1
    elif target > arr[middle]:
      low = middle+1
    else:
      return middle
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  
  if len(arr) == 0:
    return -1 # array empty
  if low <= high:
    if arr[middle] < target:
      return binary_search_recursive(arr, target, middle+1, high)
    elif arr[middle] > target:
      return binary_search_recursive(arr, target, low, middle)
    else:
      return middle
  return -1