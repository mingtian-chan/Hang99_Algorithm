import time

n = 100_000
mx = 10  # 출력 결과 너무 클 수 있으므로 mx 까지만 출력..


def func1():  # 매번 객체 새로 생성
    output_str = ""

    for i in range(n):
        output_str += str(i) + '\n'

    print(output_str[:mx*2])


def func2():  # output_lst 에 저장했다가 마지막에 한 번에 출력
    output_lst = []

    for i in range(n):
        output_lst.append(str(i) + '\n')

    output_str = "".join(output_lst[:mx])
    print(output_str)


def func3():  # 그 때 그 때 출력
    for i in range(n):
        if i < mx:
            print(i)


print("func1 start..")
s = time.time()
func1()
e = time.time()
print("func1 end..")
print(f"func1 수행 시간 : {e - s}\n")


print("func2 start..")
s = time.time()
func2()
e = time.time()
print("func2 end..")
print(f"func2 수행 시간 : {e - s}\n")

print("func3 start..")
s = time.time()
func3()
e = time.time()
print("func3 end..")
print(f"func3 수행 시간 : {e - s}")