
def lengthofLIS(nums): 
    memo = {} 
    curr_index) pair 
    subsequences = {} 
 
    def helper(prev_index, curr_index): 
        # Base case: If we've processed all elements in nums 
        if curr_index == len(nums): 
            return 0 
        if (prev_index, curr_index) in memo: 
            return memo[(prev_index, curr_index)]          
            taken = 0 
       if prev_index == -1 or nums[curr_index] > nums[prev_index]: 
            taken = 1 + helper(curr_index, curr_index + 1) 
            not_taken = helper(prev_index, curr_index + 1) 
         
       if taken > not_taken: 
            subsequences[(prev_index, curr_index)] = subsequences.get((curr_index, curr_index + 1), []) + [nums[curr_index]] 
            memo[(prev_index, curr_index)] = taken 
       else: 
            subsequences[(prev_index, curr_index)] = subsequences.get((prev_index, curr_index + 1), []) 
            memo[(prev_index, curr_index)] = not_taken 
      nums[curr_index] 
      return memo[(prev_index, curr_index)] 
     
    length = helper(-1, 0) 
    lis = subsequences.get((-1, 0), [])[::-1] 
    return length, lis 
list1 = [10, 9, 2, 5, 3, 7, 101, 18] 
length, lis = lengthofLIS(list1) 
print("Length of LIS:", length) 
print("Longest Increasing Subsequence:", lis)


