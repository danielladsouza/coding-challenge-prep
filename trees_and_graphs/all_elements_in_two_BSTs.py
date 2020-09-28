# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self, root:TreeNode) -> List[int]:
        result = []

        def helper(root:TreeNode, result) :
            if not root:
                return

            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)
            
        helper(root, result)
        print(result)
        return result
        
    def merge_lists(self, l1, l2) -> List[int]:
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

        while i<m and j < n:
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

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.inorder_traversal(root1)
        
        l2 = self.inorder_traversal(root2)
        
        l3 = self.merge_lists(l1, l2)

        return l3
        