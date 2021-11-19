"""
    LC 1634. Add Two Polynomials Represented as Linked Lists
    A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

    Each node has three attributes:

    coefficient: an integer representing the number multiplier of the term. The coefficient of the term 9x4 is 9.
    power: an integer representing the exponent. The power of the term 9x4 is 4.
    next: a pointer to the next node in the list, or null if it is the last node of the list.

    [[5,3], [4,1] , [-7,0]]
    [[5,3], [4,1] , [-7,0]]

    [[10,3], [8,1], [-14,0]
       \     \      \        \
    [[5,3], [4,1] , [-7,0]]
    [[5,4], [4,2] , [-7,0]]
                             |

    [[5,4], [5,3], [4,2], [4,1], [-14,0]]   --- result


class ListNode:
    def __init__(self, val: list[int] = None, next = None):
        self.val = val
        self.next = next

    T.C. - O(max(M.N))
    S.C. - O(max(M.N))
    M - Number of nodes in l1
    N - Number of nodes in l2
"""
def sum_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()

    while l1 or l2:
        if l1 and l2:
            if l1.val[1] == l2.val[1]:   # Same power
                if (l1.val[0] + l2.val[0]):   # Non - zero sums
                    tail.next = ListNode(list(l1.val[0] + l2.val[0], l1.val[1]))
                    tail, l1, l2 = tail.next, l1.next, l2.next
            else:
                if l1.val[1] > l2.val[1]:
                    tail.next = ListNode(
                        list(l1.val[0], l1.val[1]))
                    tail, l1 = tail.next, l1.next
                else:
                    tail.next = ListNode(
                        list(l2.val[0], l2.val[1]))
                    tail, l2 = tail.next, l2.next
            continue

        tail.next = (l1 or l2)
        tail = tail.next

    return tail.next




