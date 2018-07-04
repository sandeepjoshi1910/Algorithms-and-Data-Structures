
class TrieNode:

    def __init__(self):
        self.value = None
        self.children = [0] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.value = 0
    
    def insert(self,word):
        current = self.root
        for char in word:
            index = ord(char.lower()) - 97
            if current.children[index] == 0:
                node = TrieNode()
                node.value = char
                current.children[index] = node
            current = current.children[index]

    def wordExists(self,word):
        current = self.root

        for char in word:
            index = ord(char.lower()) - 97
            if current.children[index] != 0:
                current = current.children[index]
            else:
                return 'Not Found'
        
        return 'Found'


                