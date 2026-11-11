# Refactoring

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        pointer = self.root

        for i, char in enumerate(word):
            if char not in pointer.children:
                temp = TrieNode()
                pointer.children[char] = temp

            pointer = pointer.children[char]

        pointer.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if index == len(word):
                return node.isEnd

            if word[index] == '.':
                children = node.children.values()
            elif word[index] in node.children:
                children = [node.children[word[index]]]
            else:
                return False

            for child in children:
                if dfs(child, index + 1):
                    return True

            return False

        return dfs(self.root, 0)