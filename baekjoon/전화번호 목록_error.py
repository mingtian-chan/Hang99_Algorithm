import sys

# 처음 생각 : 문자열에 대해서 b in a 를 이용하면 좀 길긴해도 되긴 할 것 같다.
# -> 시간초과 O(n^2) 시간복잡도...



T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    lst = []
    for i in range(n):
        lst.append(sys.stdin.readline().rstrip())

    flag = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) == len(lst[j]): # 같은 수는 없으니까
                continue
            elif len(lst[i]) > len(lst[j]): # lst[i] 가 lst[j]보다 긴 경우
                if lst[j] in lst[i]:
                    flag = 1
                    break
            else: # lst[j]가 lst[i] 보다 긴 경우
                if lst[i] in lst[j]:
                    flag = 1
                    break
        if flag == 1:
            break

    if flag == 0:
        print("YES")
    if flag == 1:
        print("NO")