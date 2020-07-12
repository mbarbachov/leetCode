# XOR Operation in an Array
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start

        for i in range(1, n):
            result ^= start + 2 * i

        return result


sol = Solution()
print(sol.xorOperation(10, 5))
