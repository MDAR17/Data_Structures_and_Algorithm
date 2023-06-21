# implementation of Tree Data Structures in Python.

class Tree():
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
        
# To find the level of the Node
        
    def get_level(self):
        level=0
        itr=self.parent
        while itr:
            level+=1
            itr=itr.parent
            
        return level
        
 # To add child to a particular Node and the parent is poining toward the self where the previous node is saved
        
    def add_child(self,data):
        data.parent = self
        self.child.append(data)
        
# To print the whole Tree in a way where we can see the hiearchical structures
        
    def print(self):
        spaces='    ' * self.get_level()
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.data)
        if self.child:
            for items in self.child:
                items.print()
                
def product():
    root = Tree('Accesories')
    
    Earpods = Tree('Earpods')
    Earpods.add_child(Tree('Boat'))
    Earpods.add_child(Tree('Boult'))
    Earpods.add_child(Tree('Mivi'))
    
    Neckband = Tree('Neckband')
    Neckband.add_child(Tree('Real me'))
    Neckband.add_child(Tree('Skullcandy'))
    Neckband.add_child(Tree('Noise'))
    
    root.add_child(Earpods)
    root.add_child(Neckband)
    root.print()
    
if __name__=='__main__':
    Root = product()
    
    
    