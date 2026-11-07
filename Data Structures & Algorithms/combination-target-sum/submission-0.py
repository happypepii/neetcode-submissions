class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, remain):
            # 1. 終止條件:remain == 0 時,收集答案(記得複製 path)
            if remain == 0:
                res.append(path[:])
                return

            # 2. 剪枝條件:remain < 0 時,直接 return
            if remain < 0:
                return
            

            # 3. 從 start 開始,逐一嘗試每個數字
            for i in range(start, len(nums)):
                # 選擇:把 nums[i] 加進 path
                path.append(nums[i])
                

                # 遞迴:下一層該傳什麼 start?(提示:可重複使用同一個數)
                # remain 該怎麼更新?
                backtrack(i, remain - nums[i])
                

                # 撤銷選擇:把剛加的數字拿掉
                path.pop()

        backtrack(0, target)
        return res