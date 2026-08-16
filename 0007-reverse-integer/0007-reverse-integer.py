class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = list(str(abs(x)))
        s.reverse()
        result = sign * int("".join(s))

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result