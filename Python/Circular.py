class node:
    def __init__(self, data):
        self.data=data
        self.next=None

def count_nods(tail):
    if tail is None:
        return 0
    count=1
    current=tail.next
    while current!=tail:
        count+=1
        current=current.next
    return count