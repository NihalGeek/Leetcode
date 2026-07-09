import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        while L < R:
            M = L + (R - L) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / M)

            if hours <= h:
                R = M
            else:
                L = M + 1

        return L