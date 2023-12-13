class Solution:
    def groupAnagrams(self, lst):
        indexer = []
        new_lst = []
        for s in lst:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in indexer:
                indexer.append(sorted_s)
                new_lst.append([s])
            else:
                idx = indexer.index(sorted_s)
                new_lst[idx].append(s)
        return new_lst

solution_instance = Solution()

l = ["eat","tea","tan","ate","nat","bat"]
ans = solution_instance.groupAnagrams(l)
print(ans)