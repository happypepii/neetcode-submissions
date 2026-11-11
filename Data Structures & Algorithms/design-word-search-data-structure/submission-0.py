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
            # 1. Word 已經走完
            if index == len(word):
                return node.isEnd

            # 2. Wildcard：嘗試所有可能的 child
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True

                return False

            # 3. 一般字元：只走指定的 child
            if word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)

            return False

        return dfs(self.root, 0)