class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ')': '(', ']': '['}
        st = []

        for ch in s:
            if ch in pairs:  # closing bracket
                if st and st[-1] == pairs[ch]:
                    st.pop()
                else:
                    return False
            else:  # opening bracket
                st.append(ch)

        return not st