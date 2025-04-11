class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
#print the node:
def printNode(head):
    current_node = head 
    while current_node :
        print(current_node.data,end="->")
        current_node = current_node.next
    print("NULL")
        
#delete a node
def deleteNode(head,nodetodelete):
    if head == nodetodelete:
        return head.next
    
    current_node = head
    while current_node.next and current_node.next != nodetodelete:
        current_node = current_node.next
    
    if current_node.next is None:
        return head
    
    current_node.next = current_node.next.next
    
    return head

node1 = Node(69)
node2 = Node(23)
node3 = Node(4)
node4 = Node(45)

node1.next = node2
node2.next = node3
node3.next = node4

head = deleteNode(node1,node3)
printNode(head)
