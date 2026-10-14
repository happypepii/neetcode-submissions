class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. output[i] = product of nums / nums[i]
        # 2. track the product left of i and right of i
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = 1
        right[len(nums)-1] = 1

        for i in range(1, len(nums), 1):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        return [l * r for l, r in zip(left, right)]