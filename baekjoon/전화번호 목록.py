import sys

# 처음 생각 : 문자열에 대해서 b in a 를 이용하면 좀 길긴해도 되긴 할 것 같다.
# -> 시간초과 O(n^2) 시간복잡도...

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    flag = 0
    n = int(sys.stdin.readline().rstrip())
    lst = []
    for i in range(n):
        lst.append(sys.stdin.readline().rstrip())

    lst.sort() # 퀵소트 함 ( nlogn )
    for idx in range(len(lst)-1):
        if lst[idx] in lst[idx + 1]:
            flag = 1
            break

    if flag == 1:
        print("NO")
    else:
        print("YES")

