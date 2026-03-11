import heapq

A = [-4,3,1,0,2,5,10,8,12,9]
heapq.heapify(A)
print(A)

heapq.heappush(A,4)
print('='*20)
print(A)
minn = heapq.heappop(A)
print('='*20)
print(A,minn)

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list

C = heapsort([11,3,4,57,8,-7,0,-1])
print('='*20)
print(C)

D = [-5,4,2,1,7,0,3]
heap = []

for x in D:
    heapq.heappush(heap,x)
    print(heap,len(heap))

from collections import Counter
E = [2,3,3,3,5,7,8,8,8]
counter = Counter(E)
print(counter)

heap = []
for k,v in counter.items():
    heapq.heappush(heap,(v,k))
print(heap)