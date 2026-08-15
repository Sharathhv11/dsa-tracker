# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        previous = ListNode()
        head = previous
        p1 = list1
        p2 = list2 

        if( p1 == None ): return list2
        if( p2 == None ): return list1


        while( p1 != None and p2 != None ):
            val1 = p1.val
            val2 = p2.val

            if( val1 == val2 ):
                previous.next = p1
                previous = previous.next
                p1 = p1.next

            elif( val1 < val2 ):
                previous.next = p1
                previous = previous.next
                p1 = p1.next
            else:
                previous.next  = p2
                previous = previous.next
                p2 = p2.next

        if( p1 == None ):
            previous.next = p2
            previous = previous.next
        else:
            previous.next = p1
            previous = previous.next

        return head.next
