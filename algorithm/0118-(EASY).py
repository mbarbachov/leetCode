class Solution(object):
    @staticmethod
    def factorial(n):
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

    def combinations(self, n, k):
        return self.factorial(n) // (self.factorial(n - k) * self.factorial(k))

    def generate(self, numRows):
        pascal_triangle = []
        for n in range(numRows):
            row = []
            for k in range(n + 1):
                row.append(self.combinations(n, k))

            pascal_triangle.append(row)

        return pascal_triangle
