# implementation of Binary Tree using python

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Recursion is used to add the child where the method is called by itself
# If the data is greater then move it to right else to the left

    def add_child(self,data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
                
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right =  BinaryTree(data)

# In order to Traverse the Tree we are visiting the left ones first, then parent and then finally right ones
# This is called as In order Traversal 
               
    def inorder_trav(self):
        elements=[]
        
        if self.left:
            elements += self.left.inorder_trav()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorder_trav()
            
        return elements
    
# By using the arrangement of the tree we can easily search the data we want to find in the tree.    
    
    def search(self,data):
        if data==self.data:
            return True
        
        if data<self.data:
            if self.left:
               return self.left.search(data)
           
        if data>self.data:
            if self.right:
                return self.right.search(data)
        
        return False
   
# used to find the minimum value in the tree.  
                
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data
        
# used to find the maximum value in the tree.       
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    
# Delets the value if replacing it with its successor. if both left and right is none then no one can replace
# If either the left child or right child are present then replace the value with this and return none
# If both left and right child are present then replace the value with the minimum value of right subtree and reomve the minimum value's orginal tree by using the above two case 
    
    def delete(self,data):
        
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left == None and self.right == None:
                return None
            if self.right == None:
               return self.left
            if self.left == None:
               return self.right
            
            min_val=self.right.find_min()
            self.data=min_val
            self.right = self.right.delete(min_val)
            
        return self
    
def product_Tree(elements):
    root = BinaryTree(elements[0])
    
    for element in range(1,len(elements)):
        root.add_child(elements[element])
        
    return root

if __name__=='__main__':
    element = [17,4,1,20,9,23]
    Tree = product_Tree(element)
    print(Tree.inorder_trav())
    print(Tree.search(4))
    print(Tree.find_min())
    print(Tree.find_max())
    Tree2=product_Tree([15,12,13,14,18,16,23,21,25])
    print(Tree2.inorder_trav())
    Tree2.delete(18)
    print(Tree2.inorder_trav())