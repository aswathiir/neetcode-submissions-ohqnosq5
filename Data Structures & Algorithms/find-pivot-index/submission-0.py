class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prevsum = 0 
        totalsum = sum(nums)
        for i in range(len(nums)):
            rightsum = totalsum - nums[i] - prevsum 
            if prevsum == rightsum:
                return i
            prevsum += nums[i]
        return -1
        