class Solution(object):
    def maxProfit(self, prices):
        if not prices:  # Edge case: if prices list is empty
            return 0
        buy_price=prices[0]
        curr_profit=0
        max_profit=0
        for i in range(1,len(prices)):
            #if price at next day is higher than my buy_price then i'll try to sell that item
            if prices[i]>buy_price:
                curr_profit=prices[i]-buy_price
                #after selling that item now compare if you current profit is maximum with your previous profit if so then update your max_profit
                max_profit=max(max_profit,curr_profit)
            #if price in the next day is dropped then i'll try to buy that iteam instead of selling it as it would make loss  so, update your buy_price with lower value
            else:
                buy_price=prices[i]
        return max_profit        




                   
        