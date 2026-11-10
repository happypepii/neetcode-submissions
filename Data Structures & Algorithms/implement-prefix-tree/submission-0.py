class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        pointer = self.root

        for i, char in enumerate(word):
            if not char in pointer.children:
                temp = TrieNode()
                pointer.children[char] = temp
            
            pointer = pointer.children[char]
        
        pointer.isEnd = True
                
                
    def search(self, word: str) -> bool:
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                return False

            pointer = pointer.children[char]

        return pointer.isEnd


    def startsWith(self, prefix: str) -> bool:
        pointer = self.root

        for char in prefix:
            if char not in pointer.children:
                return False

            pointer = pointer.children[char]

        return True

        
        