class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Idea:
        ## Sort each array.
        ## If they are equal their letters will have been placed in the same order.
        if sorted(s) == sorted(t): # Time: O(nlogn)
            return True
        return False
        