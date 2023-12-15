N = int(input())
s = set(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))
for i in lst2:
    if i in s:
        # set은 hashtable으로 만들었다고 일단 생각한다면, 해시테이블에선 시간복잡도가 O(1)이 탐색시간이라서
        print(1)
    else:
        print(0)
