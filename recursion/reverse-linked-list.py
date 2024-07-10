# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 1. Maintain 3 pointers: prev, current, next.
        # 2. current.next = prev and then increment all the pointers

        prev = None
        current = head
        next_node = current.next if current else None

        while current:
            current.next = prev
            prev = current
            current = next_node
            next_node = current.next if current else None
        
        return prev

        