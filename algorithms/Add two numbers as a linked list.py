# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        if not l1 and not l2:
            return None
        lprev = None
        carriage = 0
        lresult = ListNode(carriage)
        cpointer = lresult
        lprev = lresult
        while True:
            addition = l1.val if l1 and l1.val else 0 
            addition += l2.val if l2 and l2.val else 0
            addition += carriage
            carriage, result = divmod(addition, 10)
            cpointer.val += result
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2:
                break
            cpointer = ListNode(0)
            lprev.next = cpointer
            lprev = cpointer
        if carriage:
            cpointer = ListNode(carriage)
            lprev.next = cpointer
        return lresult

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8