class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next       # pointing towards next node
        self.prev=prev       # pointing towards previous node
        
class Doubly_Linked_List():
    def __init__(self):
        self.head=None
        
# To perform insertion at beginning.If the node is empty then previous is None but for other cases previous Node 
# must be connected to the new node        
        
    def insertion_at_beg(self,data): 
        if self.head==None:
            node=Node(data,self.head)
            self.head=node
        else:
            node=Node(data,self.head)
            self.head=node
            self.head.next.prev=node
        
# To perform insertion at end. Itering through the list and node is added. The new node previous is pointed towards 
# previous node and the previous node next is pointing towards the new node. The new node next is None 
        
    def insertion_at_end(self,data):
        if self.head == None:
            node=Node(data,self.head)
            self.head=node
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data)
        itr.next=node
        node.prev=itr
    
# To remove the node at beginning by making the head node's next node as the head and the current head previoust pointer as None         
            
    def removal_at_beg(self):
        if self.head==None:
            return
        if self.head.next==None:
            self.head=None
            return
        else:
            self.head=self.head.next
            self.head.prev=None
            return
            
# To remove the node at the end by looping through and making the last node previous node previous pointer as None            
            
    def removal_at_end(self):
        if self.head==None:
            return
        
        elif self.head.next==None:
            self.head=None
            return
        
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.prev.next=None
            
# Inserts a certain list of element in the list by removing all the previous elements           
            
    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insertion_at_end(data)
        
# Fetches the length of the list.        

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count  
    
# Inserts element at a particular position by looping through and creating the new node node. The index node previous node's
# next pointer is pointing towards the new node.
        
    def insert_at(self,index,data):
        if index<0 or index > self.get_length():
            raise Exception('Invalid Index')
        elif index == 0:
            self.insertion_at_beg(data)
            return
        else:
            count=0
            itr=self.head
            while itr:
                if count == index-1:
                    node=Node(data,itr.next,itr.prev)
                    itr.next=node 
                    itr.next.prev=node
                    return  
                itr=itr.next
                count+=1
                
# removes the node at a certain position and by looping through and changing the pointer in the loop.
                
    def remove_at(self,index):
        if index<0 or index>self.get_length():
             raise Exception('Invalid Index')
        
        elif index == 0:
            self.removal_at_beg()
            return
        
        else:
            count=0
            itr=self.head
            while itr:
                if index-1 == count:
                    itr.next=itr.next.next
                    itr.next.prev=itr
                    break
                
                itr=itr.next 
                
# To demonstrate the doubly linked list 

    def print(self) :
        if self.head==None:
            print('List is empty')
            
        else:
            itr=self.head
            st=''
            while itr:
                st+='<--' + str(itr.data) +'-->'
                itr=itr.next
            print(st)
            
# To check whether the linked list is doubly linked list having all the pointer for next and previous in correct order 

    def printnp(self):
        itr=self.head
        while itr:
            try:
                print(itr.prev.data,'(',itr.data,')', itr.next.data)
            except:
                print(itr.prev,'(',itr.data,')', itr.next)
            itr=itr.next
        
            
if __name__=='__main__':
    dl=Doubly_Linked_List()
    dl.insertion_at_beg(4)
    dl.insertion_at_beg(5)
    dl.insertion_at_beg(6)
    dl.insertion_at_end(9)
    dl.print()
    dl.insert_values(['arif','kaif','affu','nadu'])
    dl.print()
    dl.insert_at(1,'monic')
    dl.print()
    dl.remove_at(1)
    dl.print()
    dl.printnp()