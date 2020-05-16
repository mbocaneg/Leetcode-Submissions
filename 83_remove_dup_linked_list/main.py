class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

# ll = ListNode(1, ListNode(1, ListNode(2, None)))
ll = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))

sol = Solution()
sol.deleteDuplicates(ll)
while(ll is not None):
    print(ll.val)
    ll = ll.next
