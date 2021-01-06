# LC 1305 - All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> List[int]:
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


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def get_all_elements(root1: TreeNode, root2: TreeNode) -> List[int]:
        # Test for edge cases
        if not all([root1, root2]):
            return []

        if not root1:
            return inorder_traversal(root2)

        if not root2:
            return inorder_traversal(root1)

        l1 = inorder_traversal(root1)
        
        l2 = inorder_traversal(root2)
        
        l3 = merge_lists(l1, l2)

        return l3


r = Solution.get_all_elements(None, None)
print(r)

