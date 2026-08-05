class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        target = n - 1

        for i in range(n-2,-1,-1):

            if( i + nums[i] >= target ):
                target = i

        return target == 0

            
        