# LC 1305 - All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
from typing import List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def inorder_traversal(root:TreeNode) -> List[int]:
        result = []

        def helper(node: TreeNode):
            # Base Case
            if not node:
                return

            helper(node.left)
            result.append(node.val)
            helper(node.right)

        # Call the helper recursive function
        helper(root)
        print(result)
        return result

    @staticmethod
    def merge_lists(l1, l2) -> List[int]:
        if len(l1) == 0:
            return l2

        if len(l2) == 0:
            return l1

        if len(l1) ==0 and len(l2) == 0:
            return []

        m = len(l1)
        n = len(l2)

        i = 0
        j = 0

        result = []

        while i < m and j < n:
            if l1[i] <= l2[j]:
                result.append(l1[i])
                i += 1
                continue

            if l2[j] < l1[i]:
                result.append(l2[j])
                j += 1
                continue

        if i == m:
            result += l2[j:]
        else:
            result += l1[i:]

        return result

    def get_all_elements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # Test for edge cases
        if root1 and not root2:
            return []

        if not root1:
            return self.inorder_traversal(root2)

        if not root2:
            return self.inorder_traversal(root1)

        l1 = self.inorder_traversal(root1)
        
        l2 = self.inorder_traversal(root2)
        
        l3 = self.merge_lists(l1, l2)

        return l3
