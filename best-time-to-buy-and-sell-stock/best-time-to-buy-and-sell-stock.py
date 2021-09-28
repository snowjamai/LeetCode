from collections import deque

class Solution:
    
    
    def maxProfit(self, prices: List[int]) -> int:
#         max_val = 0
        
#         for i in range(len(prices) - 1):
#             cur_v = prices[i]
#             tmp = prices[i + 1:]
#             sell_price = max(tmp) - cur_v
            
#             if sell_price > max_val:
#                 max_val = sell_price


        min_l = []
        max_l = [0 for _ in range(len(prices))]
        
        min_v = 100000000
        for i in range(len(prices)):
            if prices[i] < min_v:
                min_v = prices[i]
                
            min_l.append(min_v)
        
        max_v = 0
        for i in range(len(prices)):
            if prices[len(prices) - 1 -i] > max_v:
                max_v = prices[len(prices) - 1 -i]
                
            max_l[len(prices) - 1 -i] = max_v
        print(max_l)
        print(min_l)
        max_sell = 0
        for i in range(len(prices)):
            if(max_l[i] - min_l[i] > max_sell):
                max_sell = max_l[i] - min_l[i]
        
                
            
            
        return max_sell
        
            
            
        