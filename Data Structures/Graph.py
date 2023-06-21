class graph:
    def __init__(self,elements):
        self.elements = elements
        self.graph_dict ={}
        for start,end in elements:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
            
        print('The Routes are\n',self.graph_dict)
            
    def path(self,start,end,path=[]):
        path=path+[start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths=[]
        
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.path(node,end,path)
                for p in new_path:
                    if p not in paths:
                        paths.append(p)
        return paths
        
    def shortest_path(self,start,end,path=[]):
        path = path +[start]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        sp=None
        
        for node in self.graph_dict[start]:
            if node not in path:
                spl=self.shortest_path(node,end,path)
                if spl:
                    if sp is None or len(spl)<len(sp):
                        sp=spl
                    elif len(spl)==len(sp):
                        sp = [sp] + [spl]
                    
        return sp    
                
        
if __name__=='__main__':
    elements={
        ('America','Germany'),
        ('America','Europe'),
        ('Germany','Europe'),
        ('Germany','India'),
        ('Europe','India'),
        ('India','Dubai')
    }
    root=graph(elements)
    start='America'
    end='India'
    print(f'\nThe path from {start} to {end}:\n',root.path(start,end))
    print(f'\nThe shortest path from {start} to {end} :\n',root.shortest_path(start,end))
