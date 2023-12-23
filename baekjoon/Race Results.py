T = int(input())
lst = []
for _ in range(T):
    i = list(map(int, input().split()))
    lst.append(i)

lst.sort(key= lambda x : x[2])
lst.sort(key= lambda x : x[1])
lst.sort(key= lambda x : x[0])
for i in lst:
    print(f"{i[0]} {i[1]} {i[2]}")