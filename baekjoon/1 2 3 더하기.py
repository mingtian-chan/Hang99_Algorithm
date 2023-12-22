T = int(input())

lst = [1,2,4]
def memo(n):
    if n-1 < len(lst):
        return lst[n-1]
    else:
        lst.append(memo(n-1) + memo(n-2) + memo(n-3) )
        return lst[n-1]

for _ in range(T):
    n = int(input())
    print(memo(n))
