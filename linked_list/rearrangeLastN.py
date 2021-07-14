# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    """
        Last n list nodes
        Two iterator technique
        First iterator moves forward n list nodes, Iterates over the First n list nodes
        After it has traversed n list nodes, the second iterator starts traversing as step behind,
        so it can stop at the n+1 th last node

        When the first iterator reaches it's end, the second iterator is stopped at the last n+1 th last node

        We just fix the successive pointers for each of the pivotal nodes

        0 1 2 3 4 5 6

        Last 3rd node 4
        Iterator 1 travels n = 3 nodes -- it is at 3.
        Now the second iterator start travelling - when first gets to 6
        The second is at 4 - The third last node

        To move things
        Iterator1.next = l
        Iterator2 .next = None -- Assuming Iterator 2 is at the k+1 th last node

        1 2 3 4 5 6 7 8 9 10
        <---> |Start at 1 , traverse the first k nodes
        k nodes

              <------------->
                 (n - k) nodes left to traverse
      0 1 2 3 4 5 6 7 8 9 10
      <------------->
      |Start at 0, end at the k+1 th last node
                    second

        8 9 10 1 2 3 4 5 6 7

        Can there be less than n nodes in the list - Yes
        Can the list be empty - Yes
        Can n be 0 - Yes

        Inputs - Edge Cases -
                 [], 1
                 [1,2,3] 0
                 [1, 2, 3] 3
    """
    if not l or not n:
        return l

    dummy_head = ListNode(0)
    dummy_head.next = l

    first = dummy_head.next

    prev = None

    counter = 0

    # Sanity Checks
    while first and counter < n:
        counter += 1
        first = first.next

    if not first:
        return l

    second = dummy_head  # starting off 1 behind, so that we stop at the k+1th last node

    prev = None

    while first:
        prev = first
        first = first.next
        second = second.next

    prev.next, dummy_head.next, second.next = dummy_head.next, second.next, None

    return dummy_head.next
