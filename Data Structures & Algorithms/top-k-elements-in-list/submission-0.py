class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}  # number -> occurrence
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        count = {}  # occurrence -> list of numbers
        for num, freq in seen.items():
            if freq not in count:
                count[freq] = []
            count[freq].append(num)


        res = []
        for i in range(len(nums), 0, -1):
            if i in count:
                for num in count[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
