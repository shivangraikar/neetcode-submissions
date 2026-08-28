class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                results.append(i)
        return results
