# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to a lower case string without special characters
        new_string = ''
        s = s.lower()
        for char in s:
            if char.isalnum():
                new_string += char

        print(new_string)

        for i in range(int(len(new_string) / 2)):
            if new_string[i] != new_string[-1 * (i + 1)]:
                return False

        return True


sol = Solution()
print(sol.isPalindrome("""
!50;R`?o,HZT.G:v 81FY6:3y!AG ?\"J` ;P!`9W x. 'f:15IG4u\"9`K4z8`tUzw'?`.!N`P  l?A.u`?\"?996;.4?'XxeG,45fwR ,7007, Rwf\"4,GexX'?4.;699?\"?`u.A?l  P`N!.`?'wzUt`8z4K`9\"u4GI51:f' .x W9`!P; `J\"? GA!y3:6YF18 v:G.TZH,o?`R;0\"!
"""))
