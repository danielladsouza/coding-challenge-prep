# LC 1042. Flower Planting With No Adjacent
from typing import List
from collections import defaultdict
from collections import deque

# N = 4  paths = [[1,4], [1,5], [1,2], [4,5],[5,2]]

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [0]* N
        if N < 1:
            return flowers

        # Build the graph 
        # Bidirectional paths 
        graph = defaultdict(set)
        for garden_x, garden_y in paths:
            graph[garden_x - 1].add(garden_y - 1)
            graph[garden_y - 1].add(garden_x - 1)

        # Traverse graph and allocate the flowers
        # assign a flower to the ith garden
        def assign_flower(start):
        # BFS
            bfs_que = deque([start])
            while bfs_que:
                garden = bfs_que.popleft()
                if flowers[garden] != 0:
                    continue
                    
                choices = set(range(1,5))
                
                # BFS 
                for neighbor in graph[garden]:
                    # Process all the neigbors flower allocations
                    neighborFlower = flowers[neighbor]
                    
                    # Not assigned a flower to neighbor
                    if neighborFlower == 0:
                        bfs_que.append(neighbor)
                        continue
                    
                    if neighborFlower in choices:
                        choices.remove(neighborFlower)
                    
                # Now pick a flower for my current garden
                flowers[garden] = min(choices)

        # Iterate through all the gardens
        # as some may not have a direct path to other gardens
        # 4 [[1,2],[3,4]]
        for i in range(N):
            if flowers[i] == 0:
                assign_flower(i)
        return flowers

s = Solution()
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
f = s.gardenNoAdj(4, paths)
print(f)
"""
Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
"""