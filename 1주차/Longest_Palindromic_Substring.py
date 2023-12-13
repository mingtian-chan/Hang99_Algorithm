class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case 0 , 1개 -> 자기자신
        if len(s) <= 1:
            return s
        else:
            # recursive step
            # 양쪽 끝이 같다면!
            if s[0] == s[-1]:
                return s[0] + self.longestPalindrome(s[1:-1]) + s[-1]
            # 양쪽 끝이 다른 경우
            else: # abcb 라면!
                # abc를 recursive하게
                a = self.longestPalindrome(s[:-1])
                # bcb를 recursive하게
                b = self.longestPalindrome(s[1:])
                # recursive하게 한 것 중에서 긴 애를 리턴해!
                return a if len(a) >= len(b) else b


solution_instance = Solution()
s = input()
ans = solution_instance.longestPalindrome(s)
print(ans)



# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand(left: int, right: int) -> str:
#             while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
#                 left -= 1
#                 right += 1
#             return s[left + 1: right - 1]
#
#         if len(s) < 2 and s == s[::-1]:
#             return s
#
#         result = ""
#
#         for i in range(len(s) - 1):
#             # expand(i, i+1): 짝수 펠린드롬 abba, expand(i, i+2): 홀수 펠린드롬 abcba
#             # 지금까지의 result를 계속 max로 갱신하는게 신기함...
#             result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
#         return result
#
#         # 출처 : https://velog.io/@eunseokim/06.-Longest-Palindromic-Substring
