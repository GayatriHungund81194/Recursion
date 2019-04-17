def swapPairs(self, head: ListNode):
        
        if(head == None):
            return None
        if( not head.next):
            return head
        node = self.swapPairs(head.next.next)
        tmp = head
        head = head.next
        head.next = tmp
        head.next.next = node
        return head