# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    @staticmethod
    def __dict__(self):
        s=[self.val]
        head=self.next
        while head.val:
            s.append(head.val)
            head=head.next
        print(s)
        return s
class Solution(object):
    def swapPairs(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head=head.next
        def swap_head(head):
            if head is None or head.next is None:
                return 
            head=swap_head(head.next.next)
            return new_head
        head.next=swap_head(head.next)
        
        
node=ListNode(1)
node.next=ListNode(2)
node.next.next=ListNode(3)
node.next.next.next=ListNode(4)
solution=Solution()
solution.swapPairs(node)
print(node.__dict__)
s=[]
list.__len__