
matrix = [
    [1, 1, 1],  
    [1, 0, 0],  
    [1, 1, 1]
]


def printMatrix(matrix):
    for row in matrix:
        print(row)

def findZero(matrix):
    zeroIndex = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] ==0:
                zeroIndex.append([i,j])
    return zeroIndex

def makingZero(matrix,zeroIndex):
    print("Matrix AFter Making Zeros : ")
    for index in zeroIndex :
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == index[0]:
                    matrix[i][j] = 0
                if j == index[1]:
                    matrix[i][j] = 0
    return matrix
                

zeroIndex =findZero(matrix)
print("ZeroIndex : ",zeroIndex)
makingZero(matrix,zeroIndex)
printMatrix(matrix)


            
