class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        a=sum(nums)
        b=0
        nums.append(0)
        for i in range(len(nums)-1):
            if b==a-b-nums[i]:
                return i
            b+=nums[i]
        return -1