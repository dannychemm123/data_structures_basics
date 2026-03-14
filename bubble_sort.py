A = [-5,3,2,1,-3,-3,7,2,2]

def bubble_sort(arr):
    """Sort an array using bubble sort algorithm.
    
    Args:
        arr: A list of comparable elements to be sorted.
    
    Returns:
        None. Sorts the array in-place.
    """
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1],arr[i] = arr[i],arr[i-1]
bubble_sort(A)
print(A)
B = [-5,3,2,1,-3,-3,7,2,2]
def insertion_sort(arr):
    """Sort an array using insertion sort algorithm.
    
    Args:
        arr: A list of comparable elements to be sorted.
    
    Returns:
        None. Sorts the array in-place.
    """
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break

insertion_sort(B)
print(B)

def bubble_sort1(arr):
    """Sort an array using bubble sort algorithm (alternative implementation).
    
    Args:
        arr: A list of comparable elements to be sorted.
    
    Returns:
        None. Sorts the array in-place.
    """
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1]> arr[i]:
                flag = True
                arr[i-1],arr[i] = arr[i],arr[i-1]
bubble_sort1(A)
print(A)