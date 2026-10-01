class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total=0
        maxi=float('-inf')
        for i in range(len(nums)):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        
        return maxi
        