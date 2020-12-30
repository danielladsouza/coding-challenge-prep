import itertools
import heapq
from typing import Iterator, List

def sort_approximately_sorted_array(sequence: Iterator[int], 
                                    k: int) -> List[int]:
    """
        Time complexity O(nlogk) . Space complexity O(k)
    """
    min_heap: List[int] = []
    # got k covered
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    # k+1 onward
    result = []
    for x in sequence[k:]:
        # Once I push the k+1 th element, I can assume that the smallest element is the one that should be at index 0
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

if __name__ == "__main__": 
    # test is a 2 sorted array  
    test = [3, -1, 2, 6, 4, 5, 8]
    result = sort_approximately_sorted_array(test, 2)
    print(result)

