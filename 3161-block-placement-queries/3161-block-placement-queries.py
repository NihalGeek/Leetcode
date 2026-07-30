from sortedcontainers import SortedList
from typing import List


class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = min(50000, len(queries) * 3)

        obstacles = SortedList([0, MAX_X])

        # Add all obstacles first
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = FenwickTree(MAX_X + 2)

        # Build initial gaps
        for i in range(len(obstacles) - 1):
            left = obstacles[i]
            right = obstacles[i + 1]
            bit.update(right, right - left)

        ans = []

        # Process queries in reverse
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                idx = obstacles.bisect_left(x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                bit.update(right, right - left)

                obstacles.remove(x)

            else:
                _, x, sz = q

                idx = obstacles.bisect_right(x)
                prev_obstacle = obstacles[idx - 1]

                can_place = (
                    bit.query(prev_obstacle) >= sz
                    or x - prev_obstacle >= sz
                )

                ans.append(can_place)

        return ans[::-1]