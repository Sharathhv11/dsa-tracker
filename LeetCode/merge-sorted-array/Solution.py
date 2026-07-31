class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = len(nums1) - 1

        i = m - 1
        j = n - 1

        while( i >= 0 and j >= 0 ):

            if( nums1[i] >= nums2[j] ):
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else :
                nums1[k] = nums2[j]
                j-=1
                k-=1
       
        for x in range(j+1):
            nums1[x] = nums2[x]