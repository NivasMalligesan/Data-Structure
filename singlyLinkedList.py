class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(12)
node2 = Node(23)
node3 = Node(34)

node1.next = node2
node2.next = node3

current_node = node1
while current_node:
    print(current_node.data,end="->")
    current_node = current_node.next
print("NULL")
        
