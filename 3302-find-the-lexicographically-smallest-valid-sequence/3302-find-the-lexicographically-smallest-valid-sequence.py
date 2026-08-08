from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        # last[j] = the rightmost index in word1
        # that can be used to match word2[j]
        # while matching word2[j:] from right to left.
        last = [-1] * len(word2)

        i = len(word1) - 1
        j = len(word2) - 1

        # Build suffix information
        while i >= 0 and j >= 0:

            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        # canSkip means:
        # we have NOT used our one allowed mismatch yet.
        canSkip = True

        ans = []
        j = 0

        # Greedily scan word1 from left to right
        for i in range(len(word1)):

            # We already selected all characters we need
            if j == len(word2):
                break

            # Case 1:
            # Current character matches exactly.
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2:
            # Current character doesn't match.
            #
            # We can use our one allowed mismatch,
            # BUT only if there is enough room to match
            # the remaining word2 exactly.
            elif canSkip and (
                j == len(word2) - 1
                or i < last[j + 1]
            ):
                canSkip = False
                ans.append(i)
                j += 1

        # We successfully selected every character of word2
        if j == len(word2):
            return ans

        return []