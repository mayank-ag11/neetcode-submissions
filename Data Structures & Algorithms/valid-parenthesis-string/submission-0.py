class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.checkValidStringGreedy(s)
        # return self.checkValidStringStack(s)
        # return self.checkValidStringMemoization(s)
        # return self.checkValidStringRecursive(s)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def checkValidStringGreedy(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for ch in s:
            if ch == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif ch == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0: # s = ( * ) (
                leftMin = 0
        
        return leftMin == 0

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def checkValidStringStack(self, s: str) -> bool:
        left, star = [], []

        # first handle the ')' using '(' or '*'
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        # then handle the remaining '(' using '*'
        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        return not left

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def checkValidStringMemoization(self, s: str) -> bool:
        n = len(s)
        # db = {}
        db = [[None] * (n + 1) for _ in range(n + 1)]

        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            # if (i, open) in db:
            #     return db[(i, open)]

            if db[i][open] is not None:
                return db[i][open]

            ans = False
            if s[i] == '(':
                ans = dfs(i + 1, open + 1)
            elif s[i] == ')':
                ans = dfs(i + 1, open - 1)
            else:
                ans = (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
            # db[(i, open)] = ans
            db[i][open] = ans
            return ans

        return dfs(0, 0)

    # Time Complexity: O(3^n)
    # Space Complexity: O(n)
    def checkValidStringRecursive(self, s: str) -> bool:
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if s[i] == '(':
                return dfs(i + 1, open + 1)
            elif s[i] == ')':
                return dfs(i + 1, open - 1)
            else:
                return (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
        return dfs(0, 0)