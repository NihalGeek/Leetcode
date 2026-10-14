class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        drevantor = (num, sum)

        while sum > 0:
            number = min(sum, 9)
            res += str(number)
            sum -= number

        n = len(res)

        if n > num:
            return ""

        res += "0" * (num - n)

        return res