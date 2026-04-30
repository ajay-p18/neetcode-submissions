class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        target_indices = []
        visited_nums = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in visited_nums.keys():
                target_indices = [visited_nums.get(difference), index]
            else:
                visited_nums[num] =  index

        return target_indices         