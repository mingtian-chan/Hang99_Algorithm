from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        lst = [i for i in range(n)]
        return list(combinations(lst, k))
