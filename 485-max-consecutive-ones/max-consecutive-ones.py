class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        s=0
        tot=0
        for i in range(len(nums)):
            if nums[i]==1:
                s+=1
            else:
                s=0
            tot=max(tot,s)
        return tot
        