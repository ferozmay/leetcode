"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        count = 0

        third = len(nums) // 3
        for i in range(third):
            print("i is", i)
            for j in range(third, 2*third):
                print("j is", j)
                for k in range(2*third, len(nums)):
                    print("k is", k)
        