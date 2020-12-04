"""
    HR - 7 steps to solve algorithm problems - https://www.youtube.com/watch?v=GKgAVjJxh9w&feature=emb_logo
    Find common elements in two arrays
    Arrays are sorted and distinct

    
    Examples -   [1, 5, 10, 30, 56, 78, 90, 99]
                  |  |   |   |   |   |   |   |

                 [1, 2, 4, 15, 16, 56, 77, 90, 100, 120 , 170]
                  |  |  |   |   |   |  |    |   |

    Brute Force algorithm - Algorithm + run time
    Look for each element in the other array
    Time complexity - O(n**2)

    Optimize it
    Review algorithm - What are you going to do?

    idx_1 = 0
    idx_2 = 0

    iterate over both the arrays till we reach the end of one of the arrays
    comparison of values - A[idx_1] , B[idx_2]
    if we have a match - advance both pointers
    if we do not have a match advance only 1 pointer
    2 pointer approach

    Don't code prematurely

    Start Coding

"""
# Time complexity - O(N)
# Space complexity - O(N)
from typing import List

def find_common(A: List[int], B: List[int])->List[int]:
    """
        Given two monotonically increasing sequences returns the common elements between the two sequences
        Each sequence contains unique elements

    """
    idx_1 = 0
    idx_2 = 0
    matches = []

    while idx_1 < len(A) and idx_2 < len(B):
        if A[idx_1] == B[idx_2]:
            matches.append(A[idx_1])
            idx_1 += 1
            idx_2 += 1
        else:
            if A[idx_1] > B[idx_2]:
                idx_2 += 1
            else:
                idx_1 += 1
    
    return matches

A = [1, 5, 10, 30, 56, 78, 90, 99]
B = [1, 2, 4, 15, 16, 56, 77, 90, 100, 120 , 170]
result = find_common(A,B)
print(result)

