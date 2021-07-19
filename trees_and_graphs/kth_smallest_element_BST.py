# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def __init__(self):
        self.count = 0
        self.result = float('-inf')
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return
            
            if self.count < k:
                inorder(root.left)
                if self.count < k:
                    self.count += 1
                    if self.count == k:
                        self.result = root.val
                    inorder(root.right)
         
        inorder(root)
        return self.result

class Solution:
    # Iterative soltuion - Iterate to the left and add all the leftmost nodes to the stack
    def __init__(self):
        self.count = 0
        self.result = float('-inf')

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = float('-inf')

        inorder = [(root, False)]

        while inorder:
            node, leftsubtree_processed = inorder.pop()
            if node:
                if leftsubtree_processed:
                    self.count += 1
                    if self.count == k:
                        self.result = node.val
                        break
                else:
                    inorder.append((node.right, False))
                    inorder.append((node, True))
                    inorder.append((node.left, False))

        return result


# CS
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    """
        kth element in increasing order
            3
           /  \
          1.   5
               / \
              4   6


    Inorder traversal
    1 3 4 5 6

    if k = 3, return 4

        Inorder traversal , recursive
        O(k) - Time Complexity, O(N) as k --> n
        O(h) - Space Complexity - Height of the tree
    """
    result = float('-inf')
    count = 0

    # result and count are non - local
    # They cannot be updated
    def helper(n):
        """
            https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping
        """
        nonlocal result, count

        if not n:
            return

        helper(n.left)
        count += 1
        if count == k:
            result = n.value
            return
        helper(n.right)

    helper(t)
    return result


# Improve on this so as to stop iterating after finding the kth smallest element
# Iterative solution

# Bonus - Optimize - What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
