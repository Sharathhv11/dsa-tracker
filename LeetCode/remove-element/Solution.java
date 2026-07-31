class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int r = n-1;
        int i = 0;
        
        while( i <= r ){
            if( nums[i] == val ){
                int temp = nums[i];
                nums[i] = nums[r];
                nums[r] = temp;
                r--;
                continue;
            }

            i++;
        }

        return r+1;
    }
}