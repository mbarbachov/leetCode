class Solution(object):
    def isPalindrome(self, x):
        stringVersion = list(str(x))
        stringVersion.reverse()

        return ''.join(stringVersion) == str(x)
