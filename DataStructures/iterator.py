class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Iterator:
    def __init__(self,node:Node):
        self.node=node
        self.current=None
    def has_next(self):
        return  self.node is not None
    def next(self):
        if self.has_next():
            temp=self.node.next
            self.node=self.node.next
            return temp
        return None
        
node=Node(10)
node.next=Node(20)
node.next.next=Node(30)
node.next.next.next=Node(40)

print('done')