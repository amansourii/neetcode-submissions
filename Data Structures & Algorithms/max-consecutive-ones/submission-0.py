class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        current = 0
        for i in nums:
            if i == 1:
                current = current + 1
                output = max(output, current)
            else:
                current = 0
        return output