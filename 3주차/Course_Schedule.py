from collections import deque
from typing import List


class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        # 인접 리스트로 구성
        adj = [[] for _ in range(n)]
        # 선행과목 이수 : 0, 미이수 : 1 이상
        indegree = [0] * n
        # 순회 끝나면 ans 에 저장
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            # 선이수 없는 과목 먼저 다 이수하고 ( 큐에 추가 )
            if indegree[i] == 0:
                queue.append(i)
                indegree[i] -= 1

        # 큐를 돌면서 BFS
        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                # 이수 가능해졌으니, 큐에 추가
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n

