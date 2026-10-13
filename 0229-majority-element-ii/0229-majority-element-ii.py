class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq={}
        res=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        n=len(nums)
        for key,value in freq.items():
            if value>n//3:
                res.append(key)

        return res


        