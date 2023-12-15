
N, M = map(int, input().split())
d = {}

for _ in range(N):
    site, pw = input().split()
    d[site] = pw

for _ in range(M):
    site = input()
    print(d[site])
