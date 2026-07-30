class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
            
        i=j=0
        for i in range(len(neg)):
            neg[i]*=neg[i]

        for j in range(len(pos)):
            pos[j]*=pos[j]
        
        neg.reverse()

        res=[]
        i=j=0
        n=len(neg)
        m=len(pos)

        while (i<n and j<m):
            if neg[i]<pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
            
        while i<n:
            res.append(neg[i])
            i+=1
        
        while j<m:
            res.append(pos[j])
            j+=1
        
        return res