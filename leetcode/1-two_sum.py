class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers we have already passed.
        # Format: { number: its_index }
        seen = {}
        
        # We use enumerate to get both the index (i) and the value (num)
        for i, num in enumerate(nums):
            
            # Calculate the "missing piece" needed to reach the target
            complement = target - num
            
            # Check if this "missing piece" is already in our dictionary
            if complement in seen:
                # If found, return the stored index and the current index
                return [seen[complement], i]
            
            # If not found, store the current number and its index 
            # so future numbers can check against it
            seen[num] = i
            
        # The problem guarantees exactly one solution, so we don't 
        # need to worry about returning anything else here.
        return []
