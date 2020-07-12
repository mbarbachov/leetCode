# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for letter in s:
            if letter in ']})':
                if len(my_stack) == 0:
                    return False
                else:
                    last_value = my_stack.pop()
                    if f'{last_value}{letter}' not in ['()', '[]', '{}']:
                        return False
            else:
                my_stack.append(letter)

        return len(my_stack) == 0


sol = Solution()
print(sol.isValid(''))
