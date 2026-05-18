class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = set()
        for i in nums:
            if i in tmp:
                return True
            tmp.add(i)
        return False
        