# LC 126 Word Ladder II
"""
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord,
    or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

    Example
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    Explanation: There are 2 shortest transformation sequences:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
    "hit" -> "hot" -> "lot" -> "log" -> "cog"

    Test Cases
    hit hot
    hit lot hot
    hit hat hot

"""
from collections import namedtuple


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> \
            List[List[str]]:
        """
            Words can differ from each other by just one character
            To speed up the lookup of the next candidate word, we can preprocess wordList
            Use and adjacency list to identify all the possible words that can follow
            the current word and group them by the character position that they differ by.

        """
        if endWord not in wordList:
            return []

        # adjacency list
        adjacency = defaultdict(list)

        def build_adjacency_list():
            """
                T.C. O(Nd)
                S.C. O(Nd)
            """
            for word in wordList:
                for i in range(len(word)):
                    template = word[:i] + "*" + word[i + 1:]
                    adjacency[template].append(word)

        # Preprocessing of the wordList
        # Words that differ by a character at the same position grouped together
        build_adjacency_list()

        # iterative BFS
        WordWithPath = namedtuple('WordWithPath', ('word', 'path'))

        frontier = [WordWithPath(beginWord, [beginWord])]

        visited = set()
        result = []

        while frontier:
            # Process the words one level at a time

            next = []  # New nodes we are adding as we explore this level

            # Accumulation per level

            visited_this_level = set()  # Nodes we have visited as we explore this level

            for word, path in frontier:
                for i in range(len(word)):
                    template = word[:i] + "*" + word[i + 1:]
                    for adjacent_word in adjacency[
                        template]:  # Iterating over this list
                        # Only consider words/nodes we have not visited
                        if adjacent_word not in visited:
                            # Possible candidate path
                            next.append(
                                WordWithPath(adjacent_word,
                                             path + [adjacent_word]))

                            visited_this_level.add(adjacent_word)

                            if adjacent_word == endWord:  # Reached the endWord
                                result.append(path + [adjacent_word])

            if result:
                return result

            frontier = next  # Ready to process the new level
            visited = visited.union(
                visited_this_level)  # Update the master list

        return result
