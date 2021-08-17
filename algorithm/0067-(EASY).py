class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(self.bin_conv(a) + self.bin_conv(b), 'b')

    @staticmethod
    def bin_conv(num: str) -> int:
        return int(sum([int(num[i])*(2**(len(num) - i - 1)) for i in range(len(num))]))
