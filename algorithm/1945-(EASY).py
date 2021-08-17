class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted_s = ''.join([str(ord(i) - ord('a') + 1) for i in s])
        for i in range(k):
            converted_s = str(sum(list(map(int, converted_s))))

        return int(converted_s)


print(Solution().getLucky('leetcode', 2))
