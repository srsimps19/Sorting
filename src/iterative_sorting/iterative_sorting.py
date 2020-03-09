# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index 
        for num in range(i+1, len(arr)): 
            if arr[smallest_index] > arr[num]:
                smallest_index = num
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for num in range(0,len(arr)-i-1):
            if arr[num] > arr[num+1]:
                temp = arr[num]
                arr[num] = arr[num+1]
                arr[num+1] = temp 
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    return arr