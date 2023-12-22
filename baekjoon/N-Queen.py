
n = int(input())

visited = [-1] * n
cnt = 0


def is_ok_on(nth_row):

    for row in range(nth_row):
        if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
            return False
    return True


def n_queen(x):
    global cnt
    if x == n:
        cnt += 1
        return

    else:
        for i in range(n):
            visited[x] = i
            if is_ok_on(x):
                n_queen(x+1)


n_queen(0)
print(cnt)

