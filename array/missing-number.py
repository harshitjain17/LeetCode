class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1: Using sets
        numset = set(nums)
        trivialset = set()
        for i in range(len(nums)+1):
            trivialset.add(i)
        return trivialset.difference(numset).pop()
    