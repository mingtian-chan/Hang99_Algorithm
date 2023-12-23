T = int(input())

for _ in range(1, T+1):
    s = input()
    print(f"Case # {_}:")

    def dfs(idx, visited):

        visited.append(s[idx])
        if len(visited) == len(s):
            print("".join(visited))

            return
        for i in range(len(s)):
            if s[i] not in visited:
                dfs(i, visited)
                visited.pop()

    for j in range(len(s)):
        dfs(j, [])

# 반례
# 1
# abb하면 영원히 len(visit) != len(s)라서 출력이 안되고 실행이 끝남.

# 해결 -> 인덱스로 visited 를 구성
