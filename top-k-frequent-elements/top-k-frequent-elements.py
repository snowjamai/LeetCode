from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        a = sorted(a,key=a.get,reverse=True)
        cnt = 0
        answer = []
       
        for i in a:
            cnt+= 1
            answer.append(i)
            if cnt == k:
                break
                
        return answer
         
        