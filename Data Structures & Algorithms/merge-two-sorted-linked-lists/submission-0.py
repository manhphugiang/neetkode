# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        new_list = ListNode()
        curr = new_list

        list1_curr = list1
        list2_curr = list2
        while list1_curr != None and list2_curr != None:
            if list1_curr.val <= list2_curr.val:
                curr.next = list1_curr
                list1_curr = list1_curr.next
            else:
                curr.next = list2_curr
                list2_curr = list2_curr.next
            curr = curr.next
        if list1_curr is None:
            curr.next = list2_curr
        else:
            curr.next = list1_curr 
        return new_list.next