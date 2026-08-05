class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int l = 0;
        int r = 0;
        int jump = 0;

        while( r < n-1 ){


            int further = 0;
            for( int i=l; i<=r; i++ ){
                further = Math.max( i+nums[i],further);
            }

            l = r+1;
            r= further;
            jump++;
        }

        return jump;
    }
}