class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d= {}
        answer = 0
        for i in jewels:
            d[i] = 1
            
        for i in stones:
            if d.get(i):
                answer += 1
                
        return answer
                
                
                
                
            
        