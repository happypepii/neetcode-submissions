class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        def dfs(r, c, word_index):

            # 1. 找完整個 word
            if word_index == len(word):
                return True

            # 2. Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # 3. 字母不符合，或已經走過
            if board[r][c] != word[word_index]:
                return False

            # 4. 暫時標記為走過
            temp = board[r][c]
            board[r][c] = "#"

            # 5. 探索上下左右
            found = (
                dfs(r + 1, c, word_index + 1) or
                dfs(r - 1, c, word_index + 1) or
                dfs(r, c + 1, word_index + 1) or
                dfs(r, c - 1, word_index + 1)
            )

            # 6. Backtracking：還原
            board[r][c] = temp

            return found

        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
    
        return False

        
