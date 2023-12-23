T = int(input())
lst = []
for _ in range(T):
    i = input().split()
    lst.append(i)

lst.sort(key= lambda x : x[0])
lst.sort(key= lambda x : x[1])
lst.sort(key= lambda x : x[2])
for i in lst:
    print(f"{i[0]} {i[1]} {i[2]}")