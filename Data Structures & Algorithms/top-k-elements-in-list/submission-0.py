class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = defaultdict(int)
        for n in nums:
            myDict[n] += 1
        
        result = []
        while k > 0:
            maxFreq = 0
            num = 0

            for x in myDict.keys():
                currFreq = myDict[x]
                if currFreq >= maxFreq:
                    maxFreq = currFreq
                    num = x

            result.append(num)
            myDict.pop(num)
            k -= 1

        return result