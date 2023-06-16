# Hash Table using separate chainning 

class HashTable:
    def __init__(self):
        self.max=10
        self.arr1=[[] for i in range(self.max)]
        
# To get the hash function from the values
        
    def get_hash(self,key):
        total=0
        for element in key:
            total+=ord(element)
        return total % self.max

# To add the element. 
# In python there is __setitem__ method which overrides and lets us add item in the manner we add items to list 
    
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        
        found=False
        for index,element in enumerate(self.arr1[h]):
            if len(element)==2 and element[0]==key:
                self.arr1[h][index]=(key,value)
                found=True
                break
        if not found:
            self.arr1[h].append((key,value))
 
# This is to access elements from the Table 
# In Python there is __getitem__ which overrides and lets us access items in the same manner we access list
            
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr1[h]:
            if element[0]==key:
                return element[1]
            
            
# This is to delete an item from the Hash Table
# In python there is __delitem__ which overides and lets us use del key word to delete the item form the table

    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr1[h]):
            if element[0]==key:
                del self.arr1[h][index]
                
# To display the operations we create another method

    def print(self):
        print(self.arr1)
                
if __name__=='__main__':
    ht=HashTable()
    ht['Arif']=80
    ht['Kaif']=90
    ht['saad']=90
    ht['fawaz']=90
    ht.print()               # This is used to display the elements that are added to the Hash Table
    ht['Arif']=90
    ht.print()               # The display the updated value of the key Arif
    del ht['Arif']
    ht.print()               # This diplay the Hash Table after deleting the key Arif 
    ht['Arif']=88
    ht.print()               # This display the added key value pair
    print(ht['saad'])        # This display even though there is two value stored in index[10] but  it returns the value of the key
                        