class Solution {
    public int[] twoSum(int[] nums, int tar) {
         for(int i=0;i<nums.length;i++){
            for(int j=1+i;j<nums.length;j++){
                if(nums[i]+nums[j]==tar) return new int[]{i,j};
            }
        }
        return new int[]{};
    }
}