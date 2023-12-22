vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
word = input().split()

word.sort()


def check(arr):
    v_cnt, c_cnt = 0, 0  # 자음 개수, 모음 개수

    for i in arr:
        if i in vowel:
            v_cnt += 1

        else:
            c_cnt += 1

    if v_cnt >= 1 and c_cnt >= 2:
        return True

    else:
        return False


def backtracking(arr):

    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return

    for i in range(len(arr), C):
        if arr[-1] < word[i]:
            arr.append(word[i])
            backtracking(arr)
            arr.pop()


for j in range(C-L + 1):
    a = [word[j]]
    backtracking(a)
