# graph는 인접리스트의 형태로 구성됨.
# 예륻 들어, 1이랑 연결된 노드는 2 3 4야. 이런식으로.

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def dfs_recursive(node, visited):
    visited.append(node)

    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited

def dfs_stack(start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 계속 반복
    while stack:
        top = stack.pop()
        visited.append(top)

        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited
