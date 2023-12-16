from collections import deque

n, m, k = map(int,input().split())
while n != 0 and m != 0 and k != 0:
    queue = deque()
    for _ in range(1,n+1):
        queue.append(_)

    for i in range(k):
        for _ in range(m-1):
            queue.append(queue.popleft())
        ret = queue.popleft()

    print(ret)
    n, m, k = map(int,input().split())