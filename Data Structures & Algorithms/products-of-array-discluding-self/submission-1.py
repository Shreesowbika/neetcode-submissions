class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        num1=[1]*n
        num2=[1]*n
        for i in range(1,n):
            num1[i]=num1[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            num2[i]=num2[i+1]*nums[i+1]
        for i in range(n):
            num1[i]=num1[i]*num2[i]
        return num1

        