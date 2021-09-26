class graph:
    #vertices
    #edges
    
    def __init__(self):  
        self.vertices = set()
        self.edges = set()
        
    def add_vertex(self,v):
        self.vertices.add(v)
        
    def add_edge(self,e):
        for v in e:
            if not v in self.vertices: self.add_vertex(v)
        if type(e) == frozenset: self.edges.add(e)
        else: self.edges.add(frozenset(e))
    
    def add_edge(self,v1,v2):
        if not v1 in self.vertices: self.add_vertex(v1)
        if not v2 in self.vertices: self.add_vertex(v2)
        self.edges.add(frozenset({v1,v2}))
    
    def remove_vertex(self,v):
        if v in self.vertices: self.vertices.remove(v)
        
    def remove_edge(self,e):
        if e in self.edges: self.edges.remove(e)

    def get_vertices(self):
        return self.vertices
    
    def get_edges(self):
        return self.edges
    
    def neighbors(self,v):
        nbds = set()
        for x in self.edges:
            if v in x:
                for y in x:
                    if y != v: nbds.add(y)
        return nbds
                
    
    def isbipartite(self):
        A = set()
        B = set()
        #keep stack of vertices
        vertex_stack = [list(self.vertices)[0]]  
        vertices_covered=set()
     
        while vertex_stack != []:
            v = vertex_stack[0]
            vertex_stack.remove(v)
            vertices_covered.add(v)
           
            if self.neighbors(v)&A and self.neighbors(v)&B:
                #print(A)
                #print(B)
                return False
            if self.neighbors(v) & A: B.add(v)
            elif self.neighbors(v) & B: A.add(v)
            else: A.add(v)
            
            for x in self.neighbors(v):
                if not x in vertices_covered: vertex_stack.append(x)
           
            if vertex_stack == [] and self.vertices - vertices_covered != set():
                vertex_stack = [list(self.vertices-vertices_covered)[0]]
                
        return True
                
