#FIBONACCI SERIES

def fibo_dp(n): 
    memo = [-1] * (n + 1) 
    def helper(n): 
        if n == 0 or n == 1: 
            return n 
 
        if memo[n] != -1: 
            return memo[n] 
        memo[n] = helper(n-1) + helper(n-2) 
 
        return memo[n]  
    return helper(n) 

print(fibo_dp(8))  


