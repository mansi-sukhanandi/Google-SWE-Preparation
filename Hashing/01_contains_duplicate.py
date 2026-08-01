class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:  # O(1) Lookup
                return True
            seen.add(n)
        return False
