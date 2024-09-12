from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        def two_sum(nums, target):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    
        return two_sum(nums=nums, target=target)
    


l1 = [2,7,11,15] # target = 9 -> (0,1) 
l2 = [-7,7,11,15] # target = 8 -> (0,3)
l3 = [-15,7,11,15] # target = 0 -> (0,3)
l4 = [0,1,3,4,5,6,-1] # target = 0 -> (1,6)
l5 = [-3,-4,0,-2,6,9,11,0] #  = 0 -> (2, 7)

s = Solution()


print(s.twoSum(l1,9))
print(s.twoSum(l2,8))
print(s.twoSum(l3,0))
print(s.twoSum(l4,0))
print(s.twoSum(l5,0))
# print(s.twoSum(l1,9))