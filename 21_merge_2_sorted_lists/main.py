class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        print("l1 and l2 valid")

        l1_head = l1
        l2_head = l2

        merged = ListNode(0)
        merged_head = merged

        while l1_head != None or l2_head != None:
            if l1_head == None and l2_head == None:
                return merged_head.next
            elif l2_head == None:
                print("l2 is null, l1: %d" % l1_head.val)
                merged.next = ListNode(l1_head.val)
                l1_head = l1_head.next
                merged = merged.next
            elif l1_head == None:
                print("l1 is null, l2: %d" % l2_head.val)
                merged.next = ListNode(l2_head.val)
                l2_head = l2_head.next
                merged = merged.next

            elif l1_head.val <= l2_head.val:
                print("l1 < l2: %d" % l1_head.val)
                merged.next = ListNode(l1_head.val)
                l1_head = l1_head.next
                merged = merged.next
            elif l1_head == None or l1_head.val > l2_head.val:
                print("l2 < l1: %d" % l2_head.val)
                merged.next = ListNode(l2_head.val)
                l2_head = l2_head.next
                merged = merged.next
        
        return merged_head.next



head1 = ListNode(1)
head = head1

a = ListNode(2)
head1.next = a

b = ListNode(3)
a.next = b

# /////////////////////////////////////////////////////////

head2 = ListNode(1)

x = ListNode(2)
head2.next = x

y = ListNode(3)
x.next = y

# while(head1 != None):
#     print(head1.val)
#     head1 = head1.next
# print("orig head: %d" % head.val)

sol = Solution().mergeTwoLists(head1, head2)

print("solution")
while(sol != None):
    print("solution: %d" % sol.val)
    sol = sol.next