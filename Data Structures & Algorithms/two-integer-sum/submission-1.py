class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea:
        ## We can rearrange nums[i] + nums[j] = target to be target - nums[i] = nums[j] to find the indices.
        seen = dict()
        for i in range(0, len(nums)):
            if target - nums[i] in seen:
                return sorted([i, seen[target - nums[i]]]) # O(nlogn)
            seen[nums[i]] = i