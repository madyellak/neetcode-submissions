class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Idea:
        ## A set can not have duplicates.
        ## If the original array is larger than the new set, a duplicate has been removed.
        nums_check = set(nums) # Worst case O(n^2)
        if len(nums_check) < len(nums):
            return True
        return False
        