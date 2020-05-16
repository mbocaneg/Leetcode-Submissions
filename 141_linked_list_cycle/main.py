class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # def hasCycle(self, head: ListNode) -> bool:
    #     if head is None:
    #         return False
    #     slow = head
    #     fast = head.next

    #     while slow is not None:
    #         if fast is None or fast.next is None:
    #             return False
            
    #         if fast == slow:
    #             return True

    #         slow = slow.next
    #         fast = fast.next.next
        
    #     return False

    def hasCycle(self, head):
        if head is None:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

sol = Solution()

