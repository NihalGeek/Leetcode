class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                ans.append(i)
            else:
                if not ans:
                    return False
                popped=ans.pop()
                if i=="]" and popped!="[":
                    return False
                elif i=="}" and popped!="{":
                    return False
                elif i==")" and popped!="(":
                    return False
        return len(ans)==0

        
        