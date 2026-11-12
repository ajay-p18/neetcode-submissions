class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        output = []
        maxLength = 0

        nums = set(nums)

        for num in nums:

            if (num-1) not in nums:
                output.append(num)

                curr = num+1
                while curr in nums:
                    output.append(curr)
                    curr += 1
                maxLength = max(len(output), maxLength)
                output = []
        
        return maxLength

