class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.first=None
        self.last=None
    def is_empty(self):
        return self.first is None
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
            return self
        self.last.next = new_node
        self.last = new_node
        return self

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.first.value
        self.first = self.first.next
        if self.is_empty() or self.first is None:
            self.last = None
            self.first = None
        return item


queue=Queue()
queue=queue.enqueue(10).enqueue(15).enqueue(20)
print('done')