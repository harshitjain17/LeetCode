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

        # Method 2: Sum
        trivialsum, numssum = 0, 0
        for i in range(len(nums)+1):
            trivialsum += i
        for i in range(len(nums)):
            numssum += nums[i]
        
        value = (trivialsum - numssum) if trivialsum != numssum else 0
        return value