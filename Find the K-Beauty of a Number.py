class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        i = 0 
        j = k - 1
        while j < len(num_str):
            if self.is_beauty(num,num_str[i:j+1]):
                count += 1
            i += 1
            j += 1 
        return count
    
    def is_beauty(self,num:int,nums:str) -> bool:
        if int(nums) == 0:
            return False
        elif num % int(nums) == 0:
            return True
        else:
            return False
