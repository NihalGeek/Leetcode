class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum_Element=nums[0]
        minimum_Element=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            a = num
            b = maximum_Element * num
            c = minimum_Element * num
            maximum_Element=max(a,b,c)
            minimum_Element=min(a,b,c)
            res=max(res,maximum_Element)
        return res