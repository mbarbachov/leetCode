class Solution:
    def maxScore(self, s: str) -> int:
        scores = []
        for i in range(1, len(s)):
            scores.append(s[:i].count('0') + s[i:].count('1'))
            print(s[:i], s[i:])

        return max(scores)
