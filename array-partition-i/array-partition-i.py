class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a = sorted(nums)
        print(a)
        
        sum_v = 0
        
        for i in range(int(len(a) / 2)):
            num = min(a[i * 2], a[i * 2 + 1])
            print(num)
            sum_v += num
        return sum_v
        