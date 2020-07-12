# Word Pattern
class Solution:
    def checkIfEqual(self, values: list, words: list) -> bool:
        first_word = words[values[0]]
        for el in values:
            if first_word != words[el]:
                return False
        return True

    def checkThatUnique(self, indices: dict, words: list) -> bool:
        starting_indices = []
        for key in indices:
            starting_indices.append(indices[key][0])

        if len(starting_indices) == 1:
            return True

        for i in range(len(starting_indices)):
            for j in range(i + 1, len(starting_indices)):
                if words[starting_indices[i]] == words[starting_indices[j]]:
                    return False

        return True

    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split()
        indices = {}

        for i in range(len(pattern)):
            if pattern[i] in indices:
                indices[pattern[i]].append(i)
            else:
                indices[pattern[i]] = [i]

        if len(words) != len(pattern):
            return False

        for key in indices:
            if not self.checkIfEqual(indices[key], words):
                return False

        if not self.checkThatUnique(indices, words):
            return False
        return True


sol = Solution()
print(sol.wordPattern('aaa', 'aa aa aa aa'))
