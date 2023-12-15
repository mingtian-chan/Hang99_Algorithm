class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {} # 순차적으로 지나가면서 넣은 딕셔너리
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]: # 만약에 다음으로 올값이 이미 used딕셔너리에 있고, 해당 값이 시작하는 위치보다 높다면
                start = used[char] + 1 # 시작 하는 위치를 해당 value값보다 높여준다. 그러면 그전에 사용한 변수들 값과는 상관이 없어진다
            else:
                max_length = max(max_length,index - start +1) # 기존의 길이보다 높으면 두번째 매개변수가 그렇지 않으면 기존의 max_length가 유지
            used[char] = index # 값과 index값을 저장
        return max_length

