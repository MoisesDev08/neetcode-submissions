class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_table = {}
        for i, n in enumerate(nums):
          
            if n in hash_table:
                return True

            else:

                hash_table[n] = i

        return False 