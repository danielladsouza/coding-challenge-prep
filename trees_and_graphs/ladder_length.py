# L.C. 127 Word Ladder

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        """
            BFS
            Shortest path to a target word
            With each letter transformations, the length of the path gets incremented by 1
            e.g.
            hit -> hot -> lot
                +1.     +1

            hit -> lit  -> lot
                + 1.    +1

            Use a queue
            [hit, 1]
            Add all the words that can be formed by changing a single letter of this word
            and that exist in the wordList
            [(hot, 2)]
            [(dot, 3), (lot, 3)]
            [(dog,4))]
            [(log, 4)]
            [(cod, 5)]  --- TargetWord
        """
        if endWord not in wordList:
            return 0

        word_queue = deque([(beginWord, 1)])
        if beginWord in wordList:
            wordList.remove(beginWord)

        while word_queue:
            count = len(word_queue)
            while (count):
                word, path_len = word_queue.popleft()
                for i, c in enumerate(word):
                    for ascii_c in string.ascii_lowercase:
                        new_word = word[:i] + ascii_c + word[i + 1:]
                        if new_word == endWord:
                            return path_len + 1

                        if new_word in wordList:
                            word_queue.append((new_word, path_len + 1))
                            wordList.remove(new_word)  # Prevent cycles

                count -= 1

        return 0
