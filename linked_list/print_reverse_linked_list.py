from typing import List

class TreeNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_reversed_linked_list(self, head: TreeNode):
        data = []
        current = head
        
        while current != None:
            data.append(current.val)
            # advance to the next node
            current = current.next

        """
        Time complexity - O(n)
        while data:
            print(data.pop())
            print(data)
        """

        l = 0
        r = len(data) - 1

        # Time complexity o(n/2)
        # 2 pointer approach
        while l < r:
            data[l], data[r] = data[r], data[l]
            l += 1
            r -= 1

        print(data)

s = Solution()
n = TreeNode(1)
n.next = TreeNode(2)
n.next.next = TreeNode(3)

s.print_reverse_linked_list(n)

