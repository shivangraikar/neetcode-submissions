class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            m = (left + right) // 2
            result = min(result, nums[m])

            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
        return result