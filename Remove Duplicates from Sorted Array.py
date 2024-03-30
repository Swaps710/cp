class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        comp = 0
        pos = 1
        for i in range(1,len(nums)):
            if  nums[comp] != nums[i]:       
                nums[pos], nums[i] = nums[i], nums[pos]
                comp = pos
                pos += 1
        return len(set(nums))
    
