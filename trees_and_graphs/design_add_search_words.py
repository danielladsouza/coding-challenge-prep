"""
    LC 211 Design Add and Search Words Data Structure
    A TRIE data structure is well suited for this as all we need to do is store lowercase letters in a
    node. Each node can have at the most 26 children - 26 lowercase letters
    Also we can track if a specific node is the end of a word

"""
ASCII_LOWERCASE_CHARS = 26


class Node:
    def __init__(self, c: str):
        self.c = c
        self.children = [None] * ASCII_LOWERCASE_CHARS
        self.isWord = False


class WordDictionary:
    """
        A Tree data structure that contains only lowercase letters
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('\0')

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if not curr.children[ord(w) - ord('a')]:
                curr.children[ord(w) - ord('a')] = Node(w)
                # Inserting a new node with this character
            curr = curr.children[ord(w) - ord('a')]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w is '.':
                continue
            if not curr.children[ord(w) - ord('a')]:
                return None
            curr = curr.children[ord(w) - ord('a')]
        return curr.isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],["dad"],["bad"]]

# [null,null,null,null,false,true,true,true]