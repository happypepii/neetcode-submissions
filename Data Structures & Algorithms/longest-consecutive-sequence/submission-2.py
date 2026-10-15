class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for num in s:
            if num - 1 not in s:
                cur = num
                cur_len = 1

                while cur + 1 in s:
                    cur += 1
                    cur_len += 1

                max_len = max(max_len, cur_len)

        return max_len