from collections import deque

numTestCases = int(input())
for _ in range(numTestCases):
    n, m = map(int, input().split())
    priority_queue = deque(map(int, input().split()))
    cnt = 0

    while True:
        max_prior = max(priority_queue)
        curr = priority_queue.popleft()
        m -= 1

        if max_prior == curr:
            cnt += 1
            if m < 0:
                print(cnt)
                break

        else:
            priority_queue.append(curr)
            if m < 0: # 제일 앞에서 뽑힌 경우
                m = len(priority_queue) - 1


