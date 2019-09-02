class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buf_dict={}
        
        for i in range(len(nums)):
            #hey has any body been looking for me?
            if nums[i] in buf_dict:
                return [buf_dict[nums[i]],i]
            #I'll leave a note to my pair for future reference of where I am.
            else:
                buf_dict[target-nums[i]] = i
