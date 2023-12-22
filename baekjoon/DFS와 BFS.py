from collections import deque

n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
    # 여기서 sort 안해서 입력이 이상하게 들어가고 있었음.
    # 인접 리스트가 번호순이 아니라 입력 순으로 처리되어서 오답이 생성됨
    
    graph[b].sort()
    graph[a].sort()


def dfs(node, visited):
    visited.append(node)

    for adj in graph[node]:
        if adj not in visited:
            dfs(adj, visited)

    return visited


def bfs(node):
    queue = deque()
    visited = []

    queue.append(node)
    while queue:
        curr = queue.popleft()
        if curr not in visited:

            visited.append(curr)
            for i in graph[curr]:
                queue.append(i)

    return visited


ans = dfs(v,[])
for i in ans:
    print(i, end= " ")
print()
ans = bfs(v)
for i in ans:
    print(i, end= " ")
