import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            # stack : stack이 비어있으면 바로 붙여!
            # char < stack[-1] : 스택 마지막원소보다 현재 문자가 크면 바로 붙여!
            # counter[stack[-1]] : 스택의 마지막 원소가 0개면 바로 붙여!
                # ba 라면 [b] 상태에서 counter[b] = 0이니까 뒤에 b가 못 오니까 걍 붙여란 말
            # 만약 이 조건을 만족 못하면 만족 할 때까지 스택에서 빼내
            stack.append(char)
        return "".join(stack)

