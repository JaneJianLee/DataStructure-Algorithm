class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = max_global = nums[0]
        
        for i in range(1,len(nums)):
            
            max_curr = max(nums[i], nums[i]+max_curr)
            
            if max_curr > max_global:
                max_global=max_curr
                
        return max_global