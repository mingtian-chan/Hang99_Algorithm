T = int(input())

s1 = [i for i in range(T,0, -1)]
s2 = []
s3 = []

while s1 or s2:
    c, d = map(int, input().split())
    if c == 1:
        for _ in range(d):
            s2.append(s1.pop())
    else:
        for _ in range(d):
            s3.append(s2.pop())

while s3:
    print(s3.pop())
