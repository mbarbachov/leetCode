# Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num**0.5)**2 == num


sol = Solution()
print(sol.isPerfectSquare(1))
