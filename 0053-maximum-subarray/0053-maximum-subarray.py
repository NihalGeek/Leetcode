class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        summ=0
        total=float('-inf')
        for i in nums:
            summ+=i
            total=max(total,summ)
            if summ<0:
                summ=0
            
        return total
        