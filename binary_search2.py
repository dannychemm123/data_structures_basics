A = [0,1,4,6,7,8,9]

def binary_search(arr, target):
    """ 
    This function performs a binary search on a sorted array.
    
    Args:
        arr: A sorted list of elements.
        target: The element to search for.
    
    Returns:
        The index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f'{target} not found in the array'

print(binary_search(A, 7))

B = [False, False, False, False, False, True, True, True, True, True]


def binary_search_bool(arr):
    """ 
    This function performs a binary search on a sorted array of booleans.
    
    Args:
        arr: A sorted list of booleans.
    
    Returns:
        The index of the first True value.
    """
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high-low)//2
        if arr[mid] == True:
            high = mid
        else:
            low = mid + 1
    return low

print(binary_search_bool(B))

