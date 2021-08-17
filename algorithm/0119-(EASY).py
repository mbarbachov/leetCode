class Solution(object):
    @staticmethod
    def factorial(n):
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

    def combinations(self, n, k):
        return self.factorial(n) // (self.factorial(n - k) * self.factorial(k))

    def getRow(self, rowIndex):
        row = []
        for k in range(rowIndex + 1):
            row.append(self.combinations(rowIndex, k))

        return row


print(Solution().getRow(3))
