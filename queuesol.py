from collections import deque

 

class queue:

   

    def __init__(self):

        self.buffer = deque()

   

    def enqueue(self, val):

        self.buffer.appendleft(val)

        

    def dequeue(self):

        return self.buffer.pop()

   

    def is_empty(self):

        return len(self.buffer)==0

   

    def size(self):

        return len(self.buffer)

 

pq = queue()

pq.enqueue(8)

pq.enqueue(6)

pq.enqueue(7)

pq.enqueue(9)

 

pq.buffer

 

pq.size()

