class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfUsingPrefixProd(nums)
        # return self.productExceptSelfUsingDivision(nums)

    def productExceptSelfUsingPrefixProd(self, nums: List[int]) -> List[int]:
        prefixProd = [1] * len(nums)
        suffixProd = [1] * len(nums)

        for i in range(1, len(nums), 1):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(prefixProd[i] * suffixProd[i])
        return result

    def productExceptSelfUsingDivision(self, nums: List[int]) -> List[int]:
        product = 1
        productWithoutZero = 1
        count = 0
        for x in nums:
            product = product * x
            if x == 0:
                count += 1
                continue
            productWithoutZero = productWithoutZero * x

        if count > 1:
            return [0] * len(nums)

        result = []
        for x in nums:
            subRes = 1
            if x == 0:
                subRes = productWithoutZero
            else:
                subRes = int(product / x)
            result.append(subRes)

        return result