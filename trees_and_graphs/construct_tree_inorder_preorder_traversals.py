# Construct tree using inorder and preorder traversals 
# inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
# inOrder recur left, root, recur right
# preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] (DFS) root, recur left, recur right
# A binary tree node  
class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
"""Recursive function to construct binary of size len from 
   Inorder traversal inOrder[] and Preorder traversal preOrder[].  Initial values 
   of inBegin and inEnd should be 0 and len -1.  The function doesn't 
   do any error checking for cases where inorder and preorder 
   do not form a tree """
class Solution:
    def __init__(self):
        self.preIndex = 0

    def buildTree(self, inOrder, preOrder, inBegin, inEnd): 
        
        if (inBegin > inEnd): 
            return None
    
        # Pich current node from Preorder traversal using 
        # preIndex and increment preIndex 
        tNode = Node(preOrder[self.preIndex]) 
        self.preIndex += 1
    
        # If this node has no children then return 
        # Only 1 node that is the root node in the list
        if inBegin == inEnd : 
            return tNode 
    
        # Else find the index of this node in Inorder traversal 
        inIndex = self.search(inOrder, inBegin, inEnd, tNode.data) 
        
        # Using index in Inorder Traversal, construct left  
        # and right subtrees 
        tNode.left = self.buildTree(inOrder, preOrder, inBegin, inIndex-1) 
        tNode.right = self.buildTree(inOrder, preOrder, inIndex + 1, inEnd) 
    
        return tNode 
  
        # UTILITY FUNCTIONS 
        # Function to find index of vaue in arr[start...end] 
        # The function assumes that value is rpesent in inOrder[] 
        
    def search(self, arr, start, end, value): 
        for i in range(start, end + 1): 
            if arr[i] == value: 
                return i 
        
    def printInorder(self, node): 
        if node is None: 
            return 
        
        # first recur on left child 
        self.printInorder(node.left) 
        
        # then print the data of node 
        print(node.data)
    
        # now recur on right child 
        self.printInorder(node.right) 


s = Solution()
#inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
#preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 

inOrder = ['A', 'B', 'C'] 
preOrder = ['B', 'A', 'C'] 

s.preIndex = 0
root = s.buildTree(inOrder, preOrder, 0, len(inOrder)-1) 
  
# Let us test the build tree by priting Inorder traversal 
print("Inorder traversal of the constructed tree is")
s.printInorder(root) 
  
