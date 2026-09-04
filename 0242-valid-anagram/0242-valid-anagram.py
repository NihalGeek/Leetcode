class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_s={}
        for i in s:
            if i not in freq_s:
                freq_s[i]=1
            else:
                freq_s[i]+=1
        
        freq_t={}
        for j in t:
            if j not in freq_t:
                freq_t[j]=1
            else:
                freq_t[j]+=1
            
        
        return (freq_s==freq_t)
                