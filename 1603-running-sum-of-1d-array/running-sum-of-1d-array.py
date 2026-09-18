class Solution(object):
    def runningSum(self, nums):
        if not nums:
            return []
        num=[nums[0]]
        for i in range(1, len(nums)):
            num.append(num[i-1] + nums[i])
        return num

        