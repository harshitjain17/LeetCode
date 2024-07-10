class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Method 1: Using sets
        # numset = set(nums)
        # trivialset = set()
        # for i in range(len(nums)+1):
        #     trivialset.add(i)
        # return trivialset.difference(numset).pop()

        # # Method 2: Sum (difference of sum of nums and trivial)
        # trivialsum, numssum = 0, 0
        # for i in range(len(nums)+1):
        #     trivialsum += i
        # for i in range(len(nums)):
        #     numssum += nums[i]
        # value = (trivialsum - numssum) if trivialsum != numssum else 0
        # return value

        # Method 3: XOR Operation (XOR all the numbers in nums including trivial list)
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        for i in range(len(nums)+1):
            res = res ^ i
        return res