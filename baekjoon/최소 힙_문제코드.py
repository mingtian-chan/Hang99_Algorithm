import heapq
import sys

heap = []
ans = ""
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    if i == 0:
        if heap:
            ans += f"{heapq.heappop(heap)}\n"
        else:
            ans += "0\n"
    else:
        heapq.heappush(heap,i)
print(ans)


# input() : 개수가 많다면 시간 초과가 나게 됩니다.  -> sys.stdin.readline() 이용하고, 이건 \n도 받기 때문에 rstrip() 이용해줘야함.
