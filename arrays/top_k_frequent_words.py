# LC 692. Top K Frequent Words
# Space Complexity O(N)
# Time Complexity KLog(N)
from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)
        k_smallest = heapq.nsmallest(k, word_counter, key=lambda x: (-word_counter[x], x))
        return k_smallest