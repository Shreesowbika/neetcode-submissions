class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        pro=[1]*n
        a=1
        for i in range(n):
            pro[i]=a
            a=a*nums[i]
        b=1
        for i in range(n-1,-1,-1):
            pro[i]=b*pro[i]
            b=b*nums[i]
        return pro

        
        