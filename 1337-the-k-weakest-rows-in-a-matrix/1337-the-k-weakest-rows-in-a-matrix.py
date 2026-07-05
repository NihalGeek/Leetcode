class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        priority=[]
        for i,row in enumerate(mat):
            soldier_count=sum(row)
            priority.append([soldier_count,i])

        priority.sort()
        return [index for _,index in priority[:k]]