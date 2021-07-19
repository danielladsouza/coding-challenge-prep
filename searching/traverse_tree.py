"""
Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

Guaranteed constraints:
0 ≤ tree size ≤ 104.

[output] array.integer

An array that contains the values at t's nodes, ordered as described above.

"""
def traverseTree(t):
    """
          1
         /  \
        2     4
         \    /
          3  5

    Level order Traversal
    BFS
    T.C - O(N)
    S.C. - 2 ** d
    """
    if not t:
        return []

    result = []
    level_queue = deque([t])

    count = 0
    while level_queue:
        count = len(level_queue)
        while count:
            current = level_queue.popleft()
            if current:
                result.append(current.value)
                level_queue.append(current.left)
                level_queue.append(current.right)
            count -= 1

    return result