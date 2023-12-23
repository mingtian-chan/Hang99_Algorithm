import heapq
import sys

heap = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    if i == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)





