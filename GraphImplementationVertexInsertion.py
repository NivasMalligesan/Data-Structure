class Graph :
    def __init__(self,size):
        self.size = size
        self.vertex_data = [""]* size
        self.matrix = [[0] * size for _ in range(size)]
        
    def printGraph(self):
        for row in self.matrix:
            print(row)
    
    def addVertex(self,vertex,data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex] = data
        
    def addEdge(self,node1,node2):
        if 0 <= node1 < self.size and 0 <= node2 < self.size:
            self.matrix[node1][node2] = 1
            self.matrix[node2][node1] = 1
            
g = Graph(4)
g.addVertex(0, 'A')
g.addVertex(1, 'B')
g.addVertex(2, 'C')
g.addVertex(3, 'D')
g.addEdge(0, 1)  # A - B
g.addEdge(0, 2)  # A - C
g.addEdge(0, 3)  # A - D
g.addEdge(1, 2)  # B - C
g.printGraph()

