class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                
                if num1 +  num2 == target:
                    answer = [i, j]
                    return answer
        