def partition(nums):
    total_sum = sum(nums)
    if total_sum %2 != 0:
        return False

    subset_sum = total_sum // 2
    memo = {}

    def helper(current_sum, index):
        if current_sum == 0:
            return True
        
        if current_sum < 0 or index < 0:
            return False

        if (current_sum, index) in memo:
            return memo[(current_sum, index)]
        
        include = helper(current_sum - nums[index], index - 1)
        exclude = helper(current_sum, index - 1)

        memo[(current_sum, index)] = include or exclude
        return memo[(current_sum, index)]
    return helper(subset_sum, len(nums) - 1)


