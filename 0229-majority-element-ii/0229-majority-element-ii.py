from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq=Counter(nums)
        n=len(nums)
        res=[]
        for key,value in freq.items():
            if value>n//3:
                res.append(key)
        return res
    
        