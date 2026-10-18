class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = sell_price - buy_price
        # for every buy_price, check every sell_price => O(n^2)
        # sell_price as high as possible, while buy_price as low as possible

        l, r = 0, 1
        max_profit = 0

        while l < len(prices) and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                # r is the current low => buy point
                l = r
                r += 1
            else:
                # continue searching for a higher sell price
                max_profit = max(max_profit, profit)
                r += 1
            
        return max_profit
