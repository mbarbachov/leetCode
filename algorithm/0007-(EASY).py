class Solution:
    def reverse(self, x: int) -> int:
        num = (x + 1) // abs(x + 1) * int(''.join(reversed(list(str(abs(x))))))

        if -2**31 < num < 2 ** 31 - 1:
            return num
        else:
            return 0
