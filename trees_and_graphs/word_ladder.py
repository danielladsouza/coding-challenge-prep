# L.C. 127 Word Ladder
# EPI 18.7 Transform One string to another

from collections import deque, namedtuple

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

            Output - The number of words in the shortest transformation sequence

            T.C. - Undirected graph - BFS
                   Number of vertices - N
                   Number of edges (worst case) - N**2
                   O(N + N**2) = O(N**2)

                   Maximum number of edges out of a vertex - d
                   if string length d is < N
                   (Maximum number of strings that can be generated differing by 1 character)
                   T.C. - O(Nd)

            S.C. - O(N) - Used a set, word queue (max length - N)
        """
        wordSet = set(
            wordList)  # This helps improve our Time Complexity due to the O(1) lookup time

        if endWord not in wordSet:
            return 0

        StringWithDistance = namedtuple('StringWithDistance',
                                        ['candidate_string', 'word_count'])

        word_queue = deque([StringWithDistance(beginWord, 1)])

        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while word_queue:
            count = len(word_queue)
            while (count):
                word, word_count = word_queue.popleft()
                if word == endWord:
                    return word_count

                for i in range(len(word)):
                    for ascii_c in string.ascii_lowercase:
                        new_word = word[:i] + ascii_c + word[i + 1:]
                        if new_word in wordSet:
                            word_queue.append((new_word, word_count + 1))
                            wordSet.remove(new_word)  # Prevent cycles

                count -= 1

        return 0

