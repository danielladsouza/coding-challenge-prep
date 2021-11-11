"""
    L.C. 79 - Word Search
    Note : sets are mutable, be careful passing them as arguments with default empty set
           explored consists of the cells that we are actively exploring (Stack of active cells)
           If a cell is a dead end, remove it from the explored list.
           ABCD
           BBBB

           Looking for ABD

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            m x n grid
            ABCCED
              |
            current letter - A
            Traverse the grid, looking for the first letter
            [A]  - stack

            next letters - B S -- compare B
            A B

            compare againts c F
            A B C

            Character that we are looking for

            The same letter cell may not be used more than once.

            Keep track of cells visited

            Visit every cell
            With each cell as the start of my graph, traverse the graph to check for path to the destination
            DFS.

            Along the path.. the letters encountered shoudl correspond to the letters in the word

            ABCCED
            012345
            X

            ABC
            ABC


            ABB. 3

            r,c   idx
            0,0    0
            A.
            B A

            B B


            ABCCED
                    A   - Level 0 - 3 ** 0
                          Level 1 - 3 ** 1
                          Level 2 - 3 ** 2

            Imagine binary tree vs 3 - nary tree
            Each node (letter in word) , can lead us to explore 3 children
            At each level (id in word) we explore 3 children, leading us to 3 ** L (Where L is the length of the word)
            Total T.C - N * 3**L
            S.C. - O(L) + O(L) = O(L) -- Depth of the stack is L , the length of the word

        """
        m = len(board)
        n = len(board[0])
        explored = set()

        def dfs_preorder(r, c, idx):

            if (idx == len(word) - 1) and board[r][c] == word[idx]:
                return True

            if board[r][c] != word[idx]:
                return False

            if (idx == len(word) - 1):
                return False

            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            explored.add((r, c))

            for dx, dy in offsets:
                if not ((0 <= r + dx < m) and (0 <= c + dy < n) and (
                        r + dx, c + dy) not in explored):
                    continue
                if dfs_preorder(r + dx, c + dy, idx + 1):
                    return True
            explored.remove((r,c))  # explored is a stack of cells that we are actively exploring.
            return False

        for i in range(m):
            for j in range(n):
                if dfs_preorder(i, j, 0):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

"""
        C A A
        A A A
        B C D

"""
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"

s = Solution()
result = s.exist(board, word)
print(result)

"""
["A","B","C","E"]
["S","F","E","S"]
["A","D","E","E"]


"""