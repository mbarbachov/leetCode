# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        return s == t


sol = Solution()
print(sol.isAnagram('rat', 'car'))
