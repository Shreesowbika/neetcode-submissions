class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 'write' tracks the index where the next unique element should go
        write = 1
        
        # 'read' scans through the array starting from the second element
        for read in range(1, len(nums)):
            # If the current element is different from the last unique element found
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
                
        return write
