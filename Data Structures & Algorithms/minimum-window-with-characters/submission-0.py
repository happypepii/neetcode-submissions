from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have, required = 0, len(need)
        best_len, best_l = float("inf"), 0
        l = 0

        for r, c in enumerate(s):
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                lc = s[l]
                window[lc] -= 1
                if lc in need and window[lc] < need[lc]:
                    have -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]