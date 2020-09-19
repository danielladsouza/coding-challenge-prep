from typing import List

from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            # no one trusts anyone
            if N == 1:
                # I am only one 
                return 1
            return -1
        
        not_judge = {}
        possible_judge = defaultdict(list)
        
        for v in trust:
            if v[0] in possible_judge:
                possible_judge.pop(v[0], None)
                not_judge[v[0]] = True
                
            if v[1] not in not_judge:
                possible_judge[v[1]].append(v[0])
                
            not_judge[v[0]] = True
                
        if len(possible_judge) != 1:
            # There can be only one judge everyone trusts , but who trusts no one else
            return -1
        
        for key, value in possible_judge.items():
            # If I am the town judge, I need N-1 folks to trust me
            if len(value) != N-1:
                return -1
            return key

s = Solution()
print(s.findJudge(3, [[1,2], [2,3]]))
