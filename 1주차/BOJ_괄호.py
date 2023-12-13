T = int(input())
for _ in range(T):
    expr = input()
    S = []
    flag = "YES"
    for i in (expr):
        if i == "(":
            S.append(i)
        elif i == ")":
            if len(S) == 0:
                flag = "NO"
                break
            else:
                t = S.pop()
                if t != "(":
                    flag = "NO"
                    break

    if len(S) != 0:
        flag = "NO"
    print(flag)
