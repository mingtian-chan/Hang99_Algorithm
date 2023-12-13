from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []

        for i, curr in enumerate(temperatures):
            # 온도가 어제보다 낮으면 스택에 넣음
            while st and curr > temperatures[st[-1]]:
                last = st.pop()
                ans[last] = i - last
            st.append(i)

        return ans
