from itertools import combinations 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = [ i for i in range(1, n + 1)]
        a = combinations(tmp,k)
        return a
        