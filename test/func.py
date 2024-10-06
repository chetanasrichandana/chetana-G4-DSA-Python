def func(nums):
    def func1(start, end):
        memo = {}
        def helper(i):
            if i < start:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(helper(i-1), nums[i] + helper(i - 2))
            return memo[i]
        return helper(end)
    if len(nums) == 1:
        return nums[0]
    return max(func1(0, len(nums) - 2), func1(1, len(nums) - 1))

nums = [2, 3, 2]
print(func(nums))


