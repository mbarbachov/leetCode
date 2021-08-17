class Solution:
    def isHappy(self, n: int) -> bool:
        lst = []
        while True:
            num = sum(list(map(lambda x: int(x)**2, list(str(n)))))
            if num == 1: return True
            if num in lst: return False
            lst.append(num)
            n = num
        return False
