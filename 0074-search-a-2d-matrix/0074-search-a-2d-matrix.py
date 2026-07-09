class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        t=m*n
        l=0
        r=t-1
        while l<=r:
            m=l+(r-l) // 2
            i=m//n
            j=m%n
            num=matrix[i][j]
            if target==num:
                return True
            elif target<num:
                r=m-1
            elif target>num:
                l=m+1
        return False
        