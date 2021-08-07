"""
    LC 211 Design Add and Search Words Data Structure
    A TRIE data structure is well suited for this as all we need to do is store lowercase letters in a
    node. Each node can have at the most 26 children - 26 lowercase letters
    Also we can track if a specific node is the end of a word

"""
ASCII_LOWERCASE_CHARS = 26

class WordDictionary:
    """
        A Tree data structure that contains only lowercase letters
        Every node is a word dictionary
        DFS - Preorder Traversal
    """
    def __init__(self, c = '\0'):
        """
        Initialize your data structure here.
        """
        self.c = c   # This is not required as the position of the WordDictionary in the list of children can tell you it's ASCII character
                     # index 0 - the letter 'a', index 25 - the letter 'z'
                     # Useful if you want to provide str or repr

        self.children = [None] * ASCII_LOWERCASE_CHARS
        self.isWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if not curr.children[ord(w) - ord('a')]:
                curr.children[ord(w) - ord('a')] = WordDictionary(w)  # Inserting a new node with this character
            curr = curr.children[ord(w) - ord('a')]
        curr.isWord = True

    def search(self, word: str) -> bool:
        if word == "": # Exhausted the string
            return self.isWord

        for idx, w in enumerate(word):
            remainder = word[idx + 1:]
            if w == '.':   # All the children are possible candidates for this character
                for c in self.children:
                    if c and c.search(remainder):  # c could be None, we have preallocated an array of Nones
                        return True
                return False
            else:
                c = self.children[ord(w) - ord('a')]
                if c:
                    return c.search(remainder)
                else:
                    return False

"""
car 
0 c car
        ar
c Node as root
look for 
a    ar
        r
        
a Node as root
look for r
    
r Node as root word is now empty
r Node isWord
"""

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)