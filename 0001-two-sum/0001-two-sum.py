class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res in freq:
                return [freq[res],i]
            else:
                freq[nums[i]]=i

        