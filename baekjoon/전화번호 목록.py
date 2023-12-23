import sys

# 처음 생각 : 문자열에 대해서 b in a 를 이용하면 좀 길긴해도 되긴 할 것 같다.
# -> 시간초과 O(n^2) 시간복잡도...

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    lst = [sys.stdin.readline().rstrip() for _ in range(n)]

    lst.sort() # 퀵소트 함 ( nlogn )

    for idx in range(len(lst)-1):
        # 앞부분만 서로 비교함 ( prefix )
        if lst[idx] == lst[idx + 1][:len(lst[idx])]:
            print("NO")
            break
    else:
        print("YES")

