class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for i in prices:
            current_price=i
            potential_profit=current_price-min_price
            max_profit=max(max_profit,potential_profit)
            min_price=min(min_price,current_price)
        return max_profit
        