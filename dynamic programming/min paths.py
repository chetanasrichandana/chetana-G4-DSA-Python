
def minPathSum(grid, a, n): 
    memo = [] 
    for _ in range(a): 
        row = [] 
        for _ in range(n): 
            row.append(-1) 
        memo.append(row) 
         
    def helper(i, j): 
        if i == a - 1 and j == n - 1: 
            return grid[i][j] 
        if i >= a or j >= n: 
            return float('inf') 
        if memo[i][j] != -1: 
            return memo[i][j] 
        right = helper(i, j + 1)  
        down = helper(i + 1, j) 
        memo[i][j] = grid[i][j] + min(right, down) 
        return memo[i][j] 
 
    return helper(0, 0) 
grid = [ 
    [1, 3, 1], 
    [1, 5, 1], 
    [4, 2, 1] 
] 
print(minPathSum(grid, len(grid), len(grid[0]))) 


