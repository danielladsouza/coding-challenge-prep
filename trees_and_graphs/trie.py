"""
    LC 211 Design Add and Search Words Data Structure
    A TRIE data structure is well suited for this as all we need to do is store lowercase letters in a
    node. Each node can have at the most 26 children - 26 lowercase letters
    Also we can track if a specific node is the end of a word

"""
import string

class Node:
    def __init__(self, c, isWord=False):
        self.c = c
        self.isWord = isWord
        self.children = [''] * 26  # Tree Data Structure We do not need a map data structure here
        # This is a fixed sized array and the index will point to the specific character
        # The keys are known in advance . Array supports fast lookups if you know the index

        # 0 -> 'a'
        # 25 -> 'z'


class Trie:  # every Trie is a Tree with a root. We just put a space character here
             # a dummy

             # Time Complexity - O(d) - d is the length of the word
             # We are going to have to traverse d nodes in the worst case
             # Space Complexity - O(d) - number of nodes / characters in the word
             # seach and startswith - we are not using extra memory.
    def __init__(self):
        self.root = Node('\0')

    def insert(self, word : str):
        curr = self.root
        for w in word:
            if not curr.children[ord(w) - ord('a')]:
                curr.children[ord(w) - ord('a')] = Node(w)
            curr = curr.children[ord(w) - ord('a')] # Moving down the chain
        curr.isWord = True   # The very last character should be marked as True

    def search(self, word: str):
        node = getNode(word)
        return node and node.isWord

    def startsWith(self, prefix: str):
        """
            Similar to search with the exception that we are not looking for a
            complete word
        """
        return getNode(prefix)

    def getNode(self, word):
        curr = self.root
        # Traverse the TRIE. Exit if we fail to find any letter from word
        for w in word:
            if not curr.children[ord(w) - ord('a')]:
                return None
            curr = curr.children[ord(w) - ord('a')] # advance down the TRIE
        return curr



class WordDictionary:  # A WordDictionary is another name for a Trie

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def addWord(self, word: str) -> None:

    def search(self, word: str) -> bool:



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)