"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Dictionary:
        # original node → copied node
        old_to_new = {}

        # -------- PASS 1 --------
        # Create a copy of every node
        curr = head

        while curr:

            # Create a NEW node with the same value
            old_to_new[curr] = Node(curr.val)

            # Move to next original node
            curr = curr.next

        # -------- PASS 2 --------
        # Connect next and random pointers
        curr = head

        while curr:

            # Get the copied version of curr
            copy = old_to_new[curr]

            # Connect copied next pointer
            if curr.next:
                copy.next = old_to_new[curr.next]

            # Connect copied random pointer
            if curr.random:
                copy.random = old_to_new[curr.random]

            # Move through original list
            curr = curr.next

        # Return copy of the head
        if head:
            return old_to_new[head]

        return None
        