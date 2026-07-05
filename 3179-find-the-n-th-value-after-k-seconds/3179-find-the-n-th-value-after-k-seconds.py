class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        a=[1]*n
        mod=(10**9)+7
        for i in range(k):
            for j in range(1,n):
                a[j]=(a[j]+a[j-1]) % mod
        return a[-1]
        