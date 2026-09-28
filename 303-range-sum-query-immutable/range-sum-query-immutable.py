class NumArray:
    
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        s = 0

        while left <= right:
            s += self.nums[left]
            left += 1

        return s