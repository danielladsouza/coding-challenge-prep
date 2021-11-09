import heapq
def find_minimum(arr):
    # Write your code here
    heapq.heapify(arr) # T.C. O(N)
    return arr[0]   # T.C. O(1)


"""
import heapq
def find_minimum(arr):
    # Write your code here
    min_value = float('inf')
    for n in arr:
        if n < min_value:
            min_value = n
    return min_value

"""