# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def swapPairs(head: ListNode) -> ListNode:
    p1 = head
    if p1 == None:
        return p1
    p2 = head.next
    res, prev = p2, None
    if res == None:
        return p1
    while p1 != None and p2 != None:
        if prev != None:
            print(prev.next)
            prev.next = p2
        t1, t2 = None, None
        if p1.next != None:
            t1 = p1.next.next
        if p2.next != None:
            t2 = p2.next.next

        p2.next = p1
        prev = p1
        # p1.next=None
        p1, p2 = t1, t2
    # if (p2 == None) and (p1 != None):
    prev.next = p1
    return res

def main():
    head = None
    t=None
    i=0
    while i<4:
       i+=1
       if t==None:
           t = ListNode(i)
           head=t
       else:
           t.next= ListNode(i)
           t=t.next
    res=swapPairs(head)
    while res != None:
        print(res.val)
        res=res.next

main()
