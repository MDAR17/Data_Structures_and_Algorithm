# The queue data structure is implemented using a python library colleciton called deque

from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()
        
    def enque(self,value):
        self.queue.appendleft(value)
        
    def deque(self):
        self.queue.pop()
        
    def is_empty(self):
        return len(self.queue)==0
    
    def length(self):
        return print(len(self.queue))
    
    def print(self):
        return print(self.queue)
    
if __name__ == '__main__':
    q=Queue()
    q.enque({'User Name': 'Arif','Password':'ajkeu12','otp':790})
    q.enque({'User Name': 'Kaif','Password':'auieu12','otp':780})
    q.enque({'User Name': 'Karthi','Password':'aodeu12','otp':789})
    q.print()
    q.length()
    q.deque()
    q.print()
    q.length()
    print(q.is_empty())
    