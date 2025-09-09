class Solution:
    def sortedInsert(self, head, key):
        # code here
        # return head of edited linked list
        new=Node(key)
        if head is None:
            return new
        if head.data>key:
            new.next=head
            return new
        t=head
        while t.next and t.next.data<key:
            t=t.next
        new.next=t.next
        t.next=new
        return head
        
            
                
        
        
        
        
            