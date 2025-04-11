#postorder
class tree :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def postorder(head):
    if head is None:
        return 
    postorder(head.left)
    postorder(head.right)
    print(head.data,end="->")
        
node1 = tree('A')
node2 = tree('B')
node3 = tree('C')
node4 = tree('D')
node5 = tree('E')
node6 = tree('F')
node7 = tree('G')

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

postorder(node1)

