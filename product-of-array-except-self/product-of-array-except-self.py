class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_l = []
        re = 1
        
        if(nums.count(0) >= 2):
            for i in nums:
                product_l.append(0)
        else:
            re_zero = 1
            
            for i in nums:
                if i == 0:
                    re_zero = 0
                else:
                    re *= i

            for i in nums:
                if re_zero == 0:
                    if i == 0:
                        product_l.append(re)
                    else:
                        product_l.append(0)
                else:
                    product_l.append(int(re / i))

            
        return product_l
        