class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {} # map number to index
        for index, num in enumerate(nums):
            t = target - num
            if t in track:
                return [track.get(t), index]
            else:
                track[num] = index
        
        return []