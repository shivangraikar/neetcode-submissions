class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        results = []
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                results.append(i)
        return results
