class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for each in nums:
            if currentSum < 0:
                currentSum = 0
            
            currentSum += each
            maxSum = max(maxSum, currentSum)
        return maxSum