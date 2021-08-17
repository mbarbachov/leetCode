class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in set(nums):
            if nums.count(num) == 1:
                return num


print(Solution().singleNumber([4, 1, 2, 1, 2]))
