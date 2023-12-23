T = int(input())

for _ in range(1, T+1):
    s = input()
    print(f"Case # {_}:")

    def dfs(idx, visited):

        visited.append(idx)
        if len(visited) == len(s):
            ans = ""
            for char in visited:
                ans += s[char]
            print(ans)

            return
        for i in range(len(s)):
            if i not in visited:
                dfs(i, visited)
                visited.pop()

    for j in range(len(s)):
        dfs(j, [])
