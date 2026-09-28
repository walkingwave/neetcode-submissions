class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #pick the lowest price to buy 
        #pick the highest price to sell
        #can choose to make no transactions
        #return profit 

        min_price = float('inf') # set min price to highest
        max_profit = 0

        for price in prices:
            if price < min_price: 
                min_price = price # this sets min price 

            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
            


