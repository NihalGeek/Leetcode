class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            
        sorted_list=sorted(freq.items(),key=lambda x:x[1],reverse = True)
        res=[]
        for i in range(k):
            res.append(sorted_list[i][0])
        return res
        