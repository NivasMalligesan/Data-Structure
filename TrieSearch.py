class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self,word):
        node = self.trie
        for char in word :
            node= node.setdefault(char,{})
        node['$'] = True
    
    def search(self,prefix):
        node = self.trie
        for char in prefix :
            if char not in node :
                return []
            node = node[char]
        return self._collect(prefix,node,[])
    
    def _collect(self,prefix,node,word):
        if '$' in node:
            word.append(prefix)
        for char,next_node in node.items():
            if char != '$':
                self._collect(prefix+char,next_node,word)
        return word
    
trie = Trie()
while True :
    choice = int(input("1 Add \n2 Search \n3 Exit"))
    if choice == 1 :
        trie.insert(input("Enter Word :"))
    elif choice == 2 :
        print("suggestion : ",trie.search(input("Enter Prefix : ")))
    elif choice == 3 :
        break
