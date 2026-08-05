class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def rotate(start,end):
            i = start
            j = end - 1

            while( i < j ):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
            print(nums)


        n = len(nums)
        noRotation = k % n

        rotate(n-noRotation,n)
        rotate(0,n-noRotation)
        rotate(0,n)

        