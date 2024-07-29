from typing import List
import time


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:  # TWO pointer solution
            return 0

        l, r = 0, 1
        max_p = 0
        for _ in range(n - 1):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > max_p:
                    max_p = profit
            else:
                l = r
            r += 1
        return max_p


lst_ = [7,1,5,3,6,4]
s = Solution()

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
s.maxProfit(lst_)
