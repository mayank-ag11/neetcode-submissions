class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return self.longestConsecutiveHashSetOptimized(nums)
        # return self.longestConsecutiveHashSet(nums)

    def longestConsecutiveHashSetOptimized(self, nums: list[int]) -> int:
        mySet = set(nums)
        maxSeq = 0

        for num in mySet: # we iterate on the set instead of list to achieve the same thing as visited set
            if (num - 1) not in mySet:
                currSeq = 1
                while (num + currSeq) in mySet:
                    currSeq += 1
                maxSeq = max(maxSeq, currSeq)
        return maxSeq

    def longestConsecutiveHashSet(self, nums: list[int]) -> int:
        mySet = set()
        for x in nums:
            mySet.add(x)

        visited = set()
        maxSeq = 0
        for x in nums:
            if x in visited:
                continue
            visited.add(x)

            currSeq = 1
            y = x + 1
            x = x - 1
            while x in mySet:
                currSeq += 1
                visited.add(x)
                x -= 1
            while y in mySet:
                currSeq += 1
                visited.add(y)
                y += 1
            maxSeq = max(maxSeq, currSeq)

        return maxSeq