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
    """
    def __init__(self, c = '\0'):
        """
        Initialize your data structure here.
        """
        self.c = c
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
            if w[idx] == '.':   # All the children are possible candidates for this character
                for c in self.children:
                    if c and c.search(remainder):
                        return True
                return False
            else:
                c = self.children[ord(w[idx]) - ord('a')]
                if c:
                    return c.search(remainder)
                else:
                    return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)