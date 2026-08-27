
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int num=nums[i];
            int rem=target-num;
            if (seen.containsKey(rem)){
                int[] s=new int[] {seen.get(rem),i};
                return s;
                
            }
            seen.put(num,i);
    }
    return new int[] {};
}
}