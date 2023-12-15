from typing import List, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        d = Counter[nums].most_common(2)

        return d

