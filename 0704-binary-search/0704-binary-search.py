class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        N=len(nums)
        R=N-1
        if len(nums)==1 and target in nums:
            return 0
        while L<=R:
            M=L+(R-L)//2
            if nums[M]==target:
                return M
            elif nums[M]<target:
                L=M+1
            elif nums[M]>target:
                R=M-1
        else:
            return -1