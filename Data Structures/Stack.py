# In python we can implement stack using list, collections.deque and queue.LifeQueue
# In this i have used deque which is python inbuild library and from that a simple implemantation

from collections import deque

class Stack():
    def __init__(self):
        self.container=deque()
        
    def push(self,Value):
        self.container.append(Value)
        
    def pop(self):
        self.container.pop()
    
    def is_empty(self):
        return len(self.container)==0
    
    def peek(self):
        return print(self.container[-1])
    
    def length(self):
        return print(len(self.container))
    
    def print(self):
            print(self.container)
    
if __name__=='__main__':
    s=Stack()
    s.push('www.google.com')
    s.push('www.youtube.com')
    s.push('www.yahoo.com')
    s.push('www.gmail.com')
    s.print()
    s.length()
    s.peek()
    s.pop()
    s.print()
    s.length()
    s.peek()
    s.pop()
    s.pop()
    s.pop()
    s.print()
    print(s.is_empty())