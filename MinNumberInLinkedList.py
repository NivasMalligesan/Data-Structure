class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def lowest(head):
    minnum = head.data
    current_node = head
    while current_node:
        if current_node.data < minnum:
            minnum = current_node.data
        current_node = current_node.next
    return minnum

node1 = Node(69)
node2 = Node(23)
node3 = Node(4)
node4 = Node(45)

node1.next = node2
node2.next = node3
node3.next = node4

print("Min Number : ",lowest(node1))
