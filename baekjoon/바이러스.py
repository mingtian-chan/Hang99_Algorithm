
n = int(input())
m = int(input())

graph = [[ 0 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

def dfs(node):
    s = [node]
    checked = [node]
    while s:
        curr = s.pop()
        for i in range(n):
            if graph[curr][i] and i not in checked:
                s.append(i)
                checked.append(i)
    return len(checked) - 1 # 자기자신 노드는 빼줘야함.

print(dfs(0))