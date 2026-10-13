class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        summ=0
        maximum=float('-inf')
        for i in nums:
            summ+=i
            maximum=max(maximum,summ)
            if summ<0:
                summ=0
        return maximum

        
        