
n = int(input())

s = []
next = 1
ans = ""
flag = 0

for i in range(n):
    a = int(input())
    while next <= a:
        s.append(next)
        next += 1
        ans += "+\n"
    if a == s[-1]: # 젤 위에거랑 같으면
        s.pop()
        ans += "-\n"
    else:
        print("NO")
        flag = 1
        break

if not flag:
    print(ans)


