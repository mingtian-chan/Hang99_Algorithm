n = int(input())

# 일단 adjMatrix를 만들고 시작하자.
mat = [[-1 for i in range(n)] for j in range(n)]
for i in range(n):
    s = input()
    for j in range(n):
        mat[j][i] = int(s[j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

rows, cols = len(mat), len(mat[0])

cnt = 0
ans = []
for row in range(rows):
    for col in range(cols):
        # 섬이 아닌 경우 건너 뜀.
        if mat[row][col] != 1:
            continue

        stack = [(row, col)]
        cnt += 1
        apart = 0
        while stack:
            print("----------------")
            print("stack : ", stack)
            x, y = stack.pop()
            if mat[x][y] != 1:
                continue
            apart += 1
            mat[x][y] = 0
            print("x, y : ", x, y)
            print("apart : ", apart)
            print("----------------")

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue
                stack.append((nx, ny))
        ans.append(apart)

print(cnt)
ans.sort()
for i in ans:
    print(i)


