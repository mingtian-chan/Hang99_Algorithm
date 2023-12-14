from queue import PriorityQueue

numTestCases = int(input())
for _ in range(numTestCases):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    que = PriorityQueue()
    idx = 0
    for i, val in enumerate(lst):
        que.put((i, val))

    while idx < M:
        idx += 1
        que.get()[1]
    print(que.get())
