# LC 445 - Add Two Numbers ll

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_list(l: ListNode) -> ListNode:
            if not l:
                return l
            """
           
            O(N) time complexity
            """
            prev, current, next = None, l, None

            while current:
                # swap the successive nodes
                next, current.next = current.next, prev
                prev, current = current, next
            return prev

        # We reverse the linked list so that we can work with the least significant digits first
        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        # 3 4 2 7
        # 4 6 5

        # We will add the corresponding node values accounting for a carryover
        # Take into account different list lengths, and the carryover
        # while calculating sum

        dummy_result_head = result_head = ListNode()
        carryover = 0
        while l1 or l2 or carryover:
            sum_nodes = (l1.val if l1 else 0) + (
                l2.val if l2 else 0) + carryover
            carryover = sum_nodes // 10
            # The node values can be between 0 and 9 only
            new_node = ListNode(sum_nodes % 10)
            result_head.next = new_node
            result_head = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # The result list is currently reversed
        return reverse_list(dummy_result_head.next)