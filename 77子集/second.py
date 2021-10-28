class Solution:
    def combine(self, n, k):
        result = []
        combination = []
        def backtrack(index, position):
            if position == 0:
                result.append(combination[:])
                return
            for i in range(index, n + 2 - position):
                combination.append(i)
                backtrack(i + 1, position - 1)
                combination.pop()

        backtrack(1, k)
        return result
