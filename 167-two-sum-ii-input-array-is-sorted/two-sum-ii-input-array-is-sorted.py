class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen={}
        for i, num in enumerate(numbers):
            t=target-num
            if t in seen:
                return [seen[t],i+1]
            seen[num]=i+1