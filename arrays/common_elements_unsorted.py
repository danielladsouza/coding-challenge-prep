"""
    HR - https://www.youtube.com/watch?v=84UYVCluClQ&feature=emb_logo

    1. BUD - Bottlenecks, unneccessary work, duplicated work
    2. Space /Time Tradeoffs
    3. DIY - Do It Yourself

    Given two arrays that have distinct elements and they are not sorted, find the common elements between them
    Example
    A [1, 5, 12, 3, 7, 42, 11, 6]
    B [2, 5, 11, 3, 6, 41, 11, 9]  

    Brute Force - Compare each element in A with elements in B O(N2)
                  
                  Store B in a HashMap O(N)
                  Check for contains - If A in HashMap - Lookup is O(1)
                  Total time O(N)
                  Space Complexity O(N)

"""
from collections import Counter
from typing import List

def find_common(A:List[int], B:List[int])->List[int]:
    matches = []
    counter = Counter(B)   # O(N)
    for a in A:   # O (N)
        if a in counter:
            matches.append(a)

    return matches


A = [1, 5, 12, 3, 7, 42, 11, 6]

B = [2, 5, 11, 3, 6, 41, 11, 9]

result = find_common(A, B)
print(result) 

