import sys

# 처음 생각 : 문자열에 대해서 b in a 를 이용하면 좀 길긴해도 되긴 할 것 같다.
# -> 시간초과 O(n^2) 시간복잡도...

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    lst = [sys.stdin.readline().rstrip() for _ in range(n)]

    lst.sort()  # 퀵소트 함 ( nlogn )

    # 반례 : 12 랑 112가 붙어있으면 YES 출력
    for idx in range(len(lst)-1):
        if lst[idx] in lst[idx + 1]:
            print("NO")
            break
    else:
        print("YES")

