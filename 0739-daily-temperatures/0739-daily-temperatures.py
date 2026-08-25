class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=temperatures
        n=len(temps)
        stack=[]
        res=[0]*n
        for i,t in enumerate(temps):
            while stack and t>stack[-1][0]:
                prev_temp,prev_index=stack.pop()
                res[prev_index]=i-prev_index

            stack.append((t,i))
        return res
        