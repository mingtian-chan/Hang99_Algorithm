from typing import List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for i in range(len(mat)):
            cnt = mat[i].count(1)
            heapq.heappush(heap, (cnt, i))

        return [heapq.heappop(heap)[1] for i in range(k)]
