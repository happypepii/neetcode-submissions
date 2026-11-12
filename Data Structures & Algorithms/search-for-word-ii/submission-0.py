class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = None


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()

            pointer = pointer.children[char]

        pointer.isEnd = True
        pointer.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        result = []
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] == "#"):
                return

            cell = board[r][c]

            if cell not in node.children:
                return

            node = node.children[cell]

            if node.isEnd:
                result.append(node.word)
                node.isEnd = False

            temp = board[r][c]
            board[r][c] = "#"

            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)

            board[r][c] = temp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return result