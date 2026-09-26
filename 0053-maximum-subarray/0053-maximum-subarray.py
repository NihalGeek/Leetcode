class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res=nums[0]
        total=0
        for i in nums:
            if total<0:
                total=0
            total+=i
            res=max(total,res)
        return res
        