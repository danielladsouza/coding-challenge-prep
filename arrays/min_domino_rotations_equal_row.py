from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        rotations = 0
        
        def mode(l : List[int]) -> (int, int):
            count_dict = {}
            max_count = 0
            mode = 0
            
            for v in l:
                if v in count_dict:
                    count_dict[v] += 1
                else:
                    count_dict[v] = 1
                if count_dict[v] > max_count:
                    max_count = count_dict[v]
                    mode = v
                    
            return (max_count, mode)
        
        max_count_A, mode_A = mode(A)
        max_count_B, mode_B = mode(B)
        
        if max_count_A > max_count_B:
            match = A
            other = B
            mode = mode_A
        else:
            match = B
            other = A
            mode = mode_B
            
        for i,v in enumerate(match):
            if v != mode:
                if other[i] != mode:
                    return -1
                else:
                    rotations += 1
        return rotations