# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseLL(self, head):
        prev = None
        curr = head
        nextnode = curr.next if curr else None

        while curr:
            curr.next = prev
            prev = curr
            curr = nextnode
            nextnode = curr.next if curr else None
        
        return prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Base case
        if (not head or not head.next):
            return True

        slow, fast = head, head
        list2 = None

        # Step 1: Find the mid of the Linked List
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the Linked List
        list2 = slow.next
        slow.next = None
        
        # Step 3: Reverse the Linked List
        list2 = self.reverseLL(list2)

        # Step 4: Compare the two list
        while list2:
            if (list2.val != head.val):
                return False
            list2 = list2.next
            head = head.next

        return True        