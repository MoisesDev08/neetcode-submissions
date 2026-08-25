class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}
        for i, n in enumerate(nums):

            starget = target - n
            if starget in hash_table:

                return [hash_table[starget], i]
            
            hash_table[n] = i
        
        return None