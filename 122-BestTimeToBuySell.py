from typing import List
class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_price_to_buy = prices[0] 
        running_profit = 0 

        for price in prices:
            if price < best_price_to_buy:
                best_price_to_buy = price
            elif price > best_price_to_buy:
                profit = price - best_price_to_buy
                if profit > max_profit:
                    max_profit= profit
                    running_profit+=max_profit
                    best_price_to_buy = price
                    max_profit =0 

        return running_profit

if __name__ == "__main__":
    prices = [1,2,3,4,5]
    obj = Solution()
    result = obj.maxProfit(prices)
    print(result)