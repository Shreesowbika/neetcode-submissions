class Solution {
    public boolean hasDuplicate(int[] nums) {
        int a=0;
        Arrays.sort(nums);
        for (int i=1;i<nums.length;i++){
            if (nums[a]==nums[i]){
                return true;
            }
            else{
                a++;
            }
        }
        return false;
    }
}