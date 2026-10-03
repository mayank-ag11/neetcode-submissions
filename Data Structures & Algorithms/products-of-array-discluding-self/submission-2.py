class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfUsingPrefixProdOptimized(nums)
        # return self.productExceptSelfUsingPrefixProd(nums)
        # return self.productExceptSelfUsingDivision(nums)

    def productExceptSelfUsingPrefixProdOptimized(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefixProd = 1
        suffixProd = 1

        for i in range(n):
            result[i] = prefixProd
            prefixProd *= nums[i]

        for i in range(n - 1, -1, -1):
            result[i] *= suffixProd
            suffixProd *= nums[i]

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # where n is the length of nums
    def productExceptSelfUsingPrefixProd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefixProd = [1] * n
        suffixProd = [1] * n

        for i in range(1, n, 1):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = prefixProd[i] * suffixProd[i]
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # where n is the length of nums
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

        # prod, zero_cnt = 1, 0
        # for num in nums:
        #     if num:
        #         prod *= num
        #     else:
        #         zero_cnt +=  1
        # if zero_cnt > 1: return [0] * len(nums)

        # res = [0] * len(nums)
        # for i, c in enumerate(nums):
        #     if zero_cnt: res[i] = 0 if c else prod
        #     else: res[i] = prod // c
        # return res
