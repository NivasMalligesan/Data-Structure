vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]


def printAdjMatrix(matrix):
    for row in matrix:
        print(row)
        
def findingConnections(vertex,matrix):
    for i in range(len(vertex)):
        print(f"{vertex[i]}: ",end=" ")
        for j in range (len(vertex)):
            if matrix[i][j] :
                print(f"{vertex[j]}",end=" ")
        print()
        
printAdjMatrix(adjacency_matrix)
findingConnections(vertexData,adjacency_matrix)
        
