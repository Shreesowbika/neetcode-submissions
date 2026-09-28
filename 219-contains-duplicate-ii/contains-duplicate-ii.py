class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        window = set()
    
        for i, num in enumerate(nums):
        # If the number is already in the window, we found a duplicate within k distance
            if num in window:
                return True
        
        # Add the current number to the window
            window.add(num)
        
        # Keep the window size bounded to k elements
            if len(window) > k:
                window.remove(nums[i - k])
            
        return False