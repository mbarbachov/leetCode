class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 2):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


print(Solution().strStr('test', ''))
