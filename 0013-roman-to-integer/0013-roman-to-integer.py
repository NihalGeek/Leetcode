class Solution:
    def romanToInt(self, s: str) -> int:
        symbols=["I","V","X","L","C","D","M"]
        values=[1,5,10,50,100,500,1000]
        total=0
        for i in range(len(s)):
            curr=values[symbols.index(s[i])]
            if i < len(s)-1:
                nxt=values[symbols.index(s[i+1])]
                if curr>=nxt:
                    total+=curr
                else:
                    total-=curr
            else:
                total+=curr
        return total
        