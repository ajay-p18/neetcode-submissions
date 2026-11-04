class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = dict()

        for i, val in enumerate(nums):
            next_num = target - val
            if next_num in visited:
                return [visited.get(next_num), i]
            
            visited[val] = i
        
        return []
        