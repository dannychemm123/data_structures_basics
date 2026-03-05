A = [0,1,4,6,7,8,9]

class BinarySearch:
    def __init__(self, A):
        self.A = A
        self.n = len(A)   
    def search(self, x):
        low = 0
        high = self.n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.A[mid] == x:
                return mid
            elif self.A[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def __str__(self):
        return str(self.A)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, index):
        return self.A[index]
    
    def __setitem__(self, index, value):
        self.A[index] = value
    
    def __delitem__(self, index):
        del self.A[index]
    
    def __contains__(self, x):
        return self.search(x) != -1
    
    def __iter__(self):
        return iter(self.A)
    
    def __reversed__(self):
        return reversed(self.A)
    
    def reverse(self):
        """Reverses the underlying list in-place."""
        self.A.reverse()
    
bs = BinarySearch(A)
print(f"Index of 7: {bs.search(7)}")

# 1. Using the in-place reverse method
print(f"Original: {bs}")
bs.reverse()
print(f"Reversed (in-place): {bs}")

# 2. Using the reversed() function (which calls __reversed__)
# This returns an iterator, so we need to convert it to a list to print it nicely
print(f"Reversed again (iterator): {list(reversed(bs))}")