class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return self.groupAnagramsHashTable(strs)
        # return self.groupAnagramsSorting(strs)
        # return self.groupAnagramsBruteForce(strs)

# Time Complexity: O(m * n)
# Space Complexity: O(m), auxiliary space, excluding the space required for the output
# where m is the length of strs and n is the maximum length of a string in strs
    def groupAnagramsHashTable(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Time Complexity: O(m * n log n)
# Space Complexity: O(m), auxiliary space, excluding the space required for the output
# where m is the length of strs and n is the maximum length of a string in strs
    def groupAnagramsSorting(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        # result = {}

        # for s in strs:
        #     sortedStr = "".join(sorted(s))
        #     if not result.get(sortedStr):
        #         result[sortedStr] = []

        #     result[sortedStr].append(s)

        # return [x for x in result.values()]

# Time Complexity: O(m * n^2) - Time Limit Exceeded
# Space Complexity: O(m), auxiliary space, excluding the space required for the output
# where m is the length of strs and n is the maximum length of a string in strs
    def groupAnagramsBruteForce(self, strs: list[str]) -> list[list[str]]:
        result = []
        tracker = set()

        for i in range(len(strs)):
            if i in tracker:
                continue
            tracker.add(i)

            subResult = [strs[i]]
            for j in range(i + 1, len(strs)):
                if(self.isAnagram(strs[i], strs[j])):
                    tracker.add(j)
                    subResult.append(strs[j])
            result.append(subResult)

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in count)
