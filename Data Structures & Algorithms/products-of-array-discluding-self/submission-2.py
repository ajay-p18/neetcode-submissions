class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, postfix = [], []
        product_arr = []
        i = 0
        val = 1

        for num in nums:
            prefix.append(1)
            postfix.append(1)
            product_arr.append(1) #initialize everything to be blank

        while i < len(nums):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = val
            val *= nums[i]    
            i+= 1

        i = len(nums)-1
        val = 1

        while i >= 0:
            if i == len(nums)-1:
                postfix[i] = 1
            else:
                postfix[i] = val
            val *= nums[i]
            i-= 1
        
        # print(f'prefix: {prefix}')
        # print(f'postfix: {postfix}')

        for i in range(len(product_arr)):
            product_arr[i] = prefix[i] * postfix[i]

        return product_arr


