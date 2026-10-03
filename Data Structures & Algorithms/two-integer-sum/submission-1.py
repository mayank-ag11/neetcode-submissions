class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i, val in enumerate(nums):
            counterVal = target - val

            if counterVal in myDict:
                return [myDict[counterVal], i]

            myDict[val] = i

        return []