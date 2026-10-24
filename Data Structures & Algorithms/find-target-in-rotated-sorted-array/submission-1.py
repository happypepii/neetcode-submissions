class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                # from left to mid is sorted
                if nums[l] <= target < nums[mid]:
                    # target is in the left part
                    r = mid - 1
                else:
                    # target is in the right part
                    l = mid + 1
  
            else:
                # from mid to right is sorted
                if nums[mid] < target <= nums[r]:
                    # target is in the right part
                    l = mid + 1
                else:
                    # target is in the left part
                    r = mid - 1

        return -1 