# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         ln1 = list(reversed(l1))
#         ln2 = list(reversed(l2))
#         st1 = [str(x) for x in ln1]
#         st2 = [str(x) for x in ln2]
#         nw1 = "".join(st1)
#         nw2 = "".join(st2)
#         nu1 = int(nw1)
#         nu2 = int(nw2)
#         re = nu1 + nu2
#         list_of_digits = [int(i) for i in str(re)]
#         rev_num = list(reversed(list_of_digits))
#         # rein = [str(x) for x in re]
#         return rev_num
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 != None else 0
            v2 = l2.val if l2 != None else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



       
       

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
l1 = node1
node1.next = node2
node2.next = node3
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
l2 = node4
node4.next = node5
node5.next = node6

obj = Solution()
result = obj.addTwoNumbers(l1, l2)

print(result)