
class Node:
    def __init__(self,data=None,next=None):
        self.data = data  
        self.next = next  #pointer to next elements.
        
class linked_list():
    def __init__(self):
        self.head = None
    
 # this method point the new node as head to insert element at the beginning. 
        
    def insertion_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
        
# This method checks if head is empty then just adds and if not loops through the the list and adds the node at the end.
# If it retuns None then a new node is add and then previous node's next is the new node and the new node's next is None. 
        
    def insertion_at_end(self,data):
        if self.head == None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
        
# This Method Inserts certains list of data by looping through the data in the list.

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insertion_at_end(data)
             
# This method returns the length of the linked list.

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

# This method removes an element at particular index. A self index count is created.
# Through iteration the node before the index is made pointing to the index node's next node.
    
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        
        elif index==0:
            self.head=self.head.next
            return
        else:
            count = 0
            itr = self.head
            
            while itr:
                if count == index-1:
                    itr.next=itr.next.next
                    break
                itr=itr.next
                count+=1
                
# This method adds element at a particular indes. A self index using count variable is created. 
# By iterating the new node is created, its pointer are modified
                
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        
        elif index==0:
            self.insertion_at_begining(data)
            
        else:
            count=0
            itr=self.head
            while itr:
                if count == index-1:
                    node=Node(data,itr.next)
                    itr.next=node
                    break
                
                itr=itr.next
                count+=1
                
 # This method is used to make a demonstration of the linked list.               
    
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
            
        itr=self.head
        llist=''
        
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
            
        print(llist)
        
if __name__=='__main__':
    ins = linked_list()
    ins.insert_values(['dog','cat','fish','parrot'])
    ins.print()
    ins.insert_at(2,'Lion')
    ins.print()
